"""Tests of the glue code on synthetic data (the official repos need GPUs and are not exercised here)."""
import json
from pathlib import Path

import numpy as np
import pytest

from eyecode import idm_eval, prepare_subset, report, split_lerobot, video_metrics as vm


def _video(t=12, h=32, w=48, seed=0):
    rng = np.random.default_rng(seed)
    base = rng.integers(0, 255, (1, h, w, 3), dtype=np.uint8)
    return np.repeat(base, t, axis=0)


def test_identical_video_has_perfect_scores():
    v = _video()
    s = vm.score_pair(v, v, "x")
    assert s.psnr > 90 and s.ssim == pytest.approx(1.0)


def test_noise_lowers_psnr_monotonically():
    v = _video()
    rng = np.random.default_rng(1)
    last = 1e9
    for sigma in (2, 8, 32):
        g = np.clip(v + rng.normal(0, sigma, v.shape), 0, 255).astype(np.uint8)
        p = vm.score_pair(g, v).psnr
        assert p < last
        last = p
    # PSNR of gaussian noise sigma=32 should be about 20*log10(255/32) = 18.0 dB
    assert abs(last - 18.0) < 1.0


def test_conditioning_frame_is_excluded():
    v = _video()
    g = v.copy()
    g[1:] = 255 - g[1:]
    assert vm.score_pair(g, v, skip=1).psnr < 10
    assert vm.score_pair(g, v, skip=0).frames == len(v)


def test_resize_and_truncate_alignment():
    v = _video(t=12, h=32, w=48)
    g = _video(t=9, h=64, w=96)
    a, b = vm.align(g, v)
    assert a.shape == b.shape == (9, 32, 48, 3)


def test_video_roundtrip_and_end_to_end_report(tmp_path):
    gt_dir, base_dir, lora_dir, res = (tmp_path / n for n in ("gt", "base", "lora", "res"))
    rng = np.random.default_rng(0)
    for i in range(6):
        v = _video(seed=i)
        vm.write_video(v, gt_dir / f"{i}.mp4")
        for d, sigma in ((base_dir, 40), (lora_dir, 10)):
            vm.write_video(np.clip(v + rng.normal(0, sigma, v.shape), 0, 255).astype(np.uint8), d / f"{i}.mp4")
    res.mkdir()
    for name, d in (("base", base_dir), ("lora", lora_dir)):
        vm.save_scores(vm.evaluate_run(gt_dir, d), res / f"video_scores_{name}.json")
    lines, summ = report.video_section(res, ["base", "lora"])
    assert summ["lora"]["psnr_mean"] > summ["base"]["psnr_mean"]
    assert summ["paired_psnr"]["win_rate"] == 1.0 and summ["paired_psnr"]["ci95"][0] > 0
    assert (res / "video_metrics_scatter.png").exists()
    vm.side_by_side([gt_dir / "0.mp4", base_dir / "0.mp4"], ["gt", "base"], res / "sbs.mp4")
    assert vm.read_video(res / "sbs.mp4").shape[2] == 96


def test_missing_generated_videos_are_reported_not_silently_ignored(tmp_path, capsys):
    vm.write_video(_video(), tmp_path / "gt" / "a.mp4")
    vm.write_video(_video(seed=1), tmp_path / "gt" / "b.mp4")
    vm.write_video(_video(), tmp_path / "gen" / "a.mp4")
    assert len(vm.evaluate_run(tmp_path / "gt", tmp_path / "gen")) == 1
    assert "missing" in capsys.readouterr().out
    with pytest.raises(RuntimeError):
        vm.evaluate_run(tmp_path / "gt", tmp_path / "empty")


def test_split_is_disjoint_deterministic():
    names = [f"{i}.mp4" for i in range(40)]
    a = prepare_subset.split(names, 24, 8, 0)
    assert a == prepare_subset.split(names, 24, 8, 0)
    assert not set(a[0]) & set(a[1]) and len(a[0]) == 24 and len(a[1]) == 8
    with pytest.raises(ValueError):
        prepare_subset.split(names, 35, 10, 0)


def test_prepare_subset_cli_files(tmp_path, monkeypatch):
    src = tmp_path / "src"
    (src / "videos").mkdir(parents=True)
    rows = ["file_name,text"]
    for i in range(5):
        vm.write_video(_video(seed=i), src / "videos" / f"{i}.mp4")
        rows.append(f'{i}.mp4,"Use the hand, then place {i}"')
    (src / "metadata.csv").write_text("\n".join(rows) + "\n")
    monkeypatch.setattr("sys.argv", ["x", "--src", str(src), "--out_train", str(tmp_path / "tr"),
                                      "--out_eval", str(tmp_path / "ev"), "--n_train", "3", "--n_eval", "2"])
    prepare_subset.main()
    meta = prepare_subset.read_metadata(tmp_path / "tr" / "metadata.csv")
    assert len(meta) == 3 and all("," in p for p in meta.values())  # commas inside prompts survive
    batch = json.loads((tmp_path / "ev" / "batch_input_template.json").read_text())
    assert len(batch) == 2 and Path(batch[0]["input_video"]).exists()


def test_idm_errors_beat_or_lose_to_baselines_correctly():
    rng = np.random.default_rng(0)
    gt = {0: rng.normal(size=(50, 6)), 1: rng.normal(size=(40, 6))}
    groups = {"left": (0, 3), "right": (3, 6)}
    perfect = idm_eval.action_errors(gt, gt, np.zeros(6), groups)
    assert perfect["idm"]["mse"] == 0 and perfect["mean_action"]["mse"] > 0.5
    noisy = {k: v + 0.1 * rng.normal(size=v.shape) for k, v in gt.items()}
    r = idm_eval.action_errors(noisy, gt, np.zeros(6), groups, hold=gt)
    assert 0.005 < r["idm"]["mse"] < 0.02 and r["state_hold"]["mse"] == 0
    assert set(r["idm"]["per_group_mse"]) == {"left", "right"}
    with pytest.raises(ValueError):
        idm_eval.action_errors({0: gt[0][:10]}, gt, np.zeros(6), groups)


def test_split_lerobot_keeps_only_requested_episodes(tmp_path):
    src = tmp_path / "ds"
    (src / "meta").mkdir(parents=True)
    (src / "data/chunk-000").mkdir(parents=True)
    (src / "videos/chunk-000/cam").mkdir(parents=True)
    (src / "meta/episodes.jsonl").write_text("".join(json.dumps({"episode_index": i, "length": 10 + i}) + "\n" for i in range(5)))
    (src / "meta/info.json").write_text(json.dumps({"total_episodes": 5, "total_frames": 60}))
    (src / "meta/stats.json").write_text("{}")
    for i in range(5):
        (src / f"data/chunk-000/episode_{i:06d}.parquet").write_bytes(b"x")
        (src / f"videos/chunk-000/cam/episode_{i:06d}.mp4").write_bytes(b"x")
    split_lerobot.make_subset(src, tmp_path / "val", [4])
    info = json.loads((tmp_path / "val/meta/info.json").read_text())
    assert info == {"total_episodes": 1, "total_frames": 14}
    assert [p.name for p in (tmp_path / "val/data/chunk-000").iterdir()] == ["episode_000004.parquet"]
    with pytest.raises(ValueError):
        split_lerobot.make_subset(src, tmp_path / "bad", [9])


def test_parquet_loader_roundtrip(tmp_path):
    pd = pytest.importorskip("pandas")
    pytest.importorskip("pyarrow")
    d = tmp_path / "data/chunk-000"
    d.mkdir(parents=True)
    arr = np.arange(12, dtype=float).reshape(4, 3)
    pd.DataFrame({"action": list(arr)}).to_parquet(d / "episode_000002.parquet")
    out = idm_eval.load_episode_arrays(tmp_path)
    assert list(out) == [2] and np.allclose(out[2], arr)
