"""Reference-based video metrics: generated video vs the ground-truth video of the same episode.

The first `skip` frames are the conditioning frame(s) given to the model, i.e. copied from the
ground truth, so they are excluded to avoid inflating the scores.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import cv2
import numpy as np
from skimage.metrics import peak_signal_noise_ratio, structural_similarity


def read_video(path: str | Path) -> np.ndarray:
    """Decode to (T, H, W, 3) uint8 RGB."""
    cap = cv2.VideoCapture(str(path))
    frames = []
    while True:
        ok, f = cap.read()
        if not ok:
            break
        frames.append(cv2.cvtColor(f, cv2.COLOR_BGR2RGB))
    cap.release()
    if not frames:
        raise RuntimeError(f"no frames decoded from {path}")
    return np.stack(frames)


def write_video(frames: np.ndarray, path: str | Path, fps: int = 16) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    h, w = frames.shape[1:3]
    vw = cv2.VideoWriter(str(path), cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))
    for f in frames:
        vw.write(cv2.cvtColor(f, cv2.COLOR_RGB2BGR))
    vw.release()


def align(gen: np.ndarray, gt: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Resize `gen` to the GT resolution and truncate both to the common number of frames."""
    t = min(len(gen), len(gt))
    gen, gt = gen[:t], gt[:t]
    if gen.shape[1:3] != gt.shape[1:3]:
        h, w = gt.shape[1:3]
        gen = np.stack([cv2.resize(f, (w, h), interpolation=cv2.INTER_AREA) for f in gen])
    return gen, gt


@dataclass
class VideoScore:
    name: str
    psnr: float
    ssim: float
    frames: int
    psnr_by_frame: list[float]


def score_pair(gen: np.ndarray, gt: np.ndarray, name: str = "", skip: int = 1) -> VideoScore:
    gen, gt = align(gen, gt)
    if len(gen) <= skip:
        raise ValueError(f"{name}: only {len(gen)} frames, cannot skip {skip}")
    psnrs, ssims = [], []
    for g, r in zip(gen[skip:], gt[skip:]):
        psnrs.append(min(peak_signal_noise_ratio(r, g, data_range=255), 100.0))  # identical frames -> inf; cap
        ssims.append(structural_similarity(r, g, channel_axis=-1, data_range=255))
    return VideoScore(name, float(np.mean(psnrs)), float(np.mean(ssims)), len(psnrs), [float(p) for p in psnrs])


def evaluate_run(gt_dir: str | Path, gen_dir: str | Path, skip: int = 1) -> list[VideoScore]:
    """Score every GT video that has a same-named generated video in `gen_dir`; report missing ones."""
    gt_dir, gen_dir = Path(gt_dir), Path(gen_dir)
    scores, missing = [], []
    for gt_path in sorted(gt_dir.glob("*.mp4")):
        gen_path = gen_dir / gt_path.name
        if not gen_path.exists():
            missing.append(gt_path.name)
            continue
        scores.append(score_pair(read_video(gen_path), read_video(gt_path), gt_path.name, skip))
    if missing:
        print(f"[warn] {len(missing)} videos missing in {gen_dir}: {missing[:5]}...")
    if not scores:
        raise RuntimeError(f"no generated videos found in {gen_dir}")
    return scores


def summarize(scores: list[VideoScore]) -> dict:
    p, s = np.array([x.psnr for x in scores]), np.array([x.ssim for x in scores])
    return {"n": len(scores), "psnr_mean": float(p.mean()), "psnr_std": float(p.std(ddof=1)) if len(p) > 1 else 0.0,
            "ssim_mean": float(s.mean()), "ssim_std": float(s.std(ddof=1)) if len(s) > 1 else 0.0}


def paired_comparison(a: list[VideoScore], b: list[VideoScore], metric: str = "psnr", n_boot: int = 5000,
                      seed: int = 0) -> dict:
    """b - a on videos present in both runs: mean diff, 95% bootstrap CI, win rate."""
    da = {x.name: getattr(x, metric) for x in a}
    db = {x.name: getattr(x, metric) for x in b}
    names = sorted(set(da) & set(db))
    if not names:
        raise ValueError("no common videos")
    diff = np.array([db[n] - da[n] for n in names])
    rng = np.random.default_rng(seed)
    boots = rng.choice(diff, (n_boot, len(diff)), replace=True).mean(axis=1)
    return {"metric": metric, "n": len(diff), "mean_diff": float(diff.mean()),
            "ci95": [float(np.percentile(boots, 2.5)), float(np.percentile(boots, 97.5))],
            "win_rate": float((diff > 0).mean())}


def side_by_side(paths: list[str | Path], labels: list[str], out: str | Path, fps: int = 16) -> None:
    """Concatenate videos horizontally (resized to the first one) with a text label on each panel."""
    vids = [read_video(p) for p in paths]
    h, w = vids[0].shape[1:3]
    t = min(len(v) for v in vids)
    panels = []
    for v, lab in zip(vids, labels):
        v = np.stack([cv2.resize(f, (w, h), interpolation=cv2.INTER_AREA) for f in v[:t]]) if v.shape[1:3] != (h, w) else v[:t]
        v = v.copy()
        for f in v:
            cv2.putText(f, lab, (8, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 3, cv2.LINE_AA)
            cv2.putText(f, lab, (8, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1, cv2.LINE_AA)
        panels.append(v)
    write_video(np.concatenate(panels, axis=2), out, fps)


def save_scores(scores: list[VideoScore], path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps([s.__dict__ for s in scores], indent=1))


def load_scores(path: str | Path) -> list[VideoScore]:
    return [VideoScore(**d) for d in json.loads(Path(path).read_text())]
