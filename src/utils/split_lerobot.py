"""Hold out episodes of a LeRobot-format dataset (the format GR00T-Dreams' IDM code reads).

Episode ids are kept (no renumbering), so parquet/video files are copied untouched; only
`meta/episodes.jsonl` and the totals in `meta/info.json` are rewritten. `stats.json` is copied as is
(it was computed on all episodes - a small, documented leak into the normalisation statistics).
"""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


def _episode_files(root: Path, ep: int) -> list[Path]:
    pats = [f"data/chunk-*/episode_{ep:06d}.parquet", f"videos/chunk-*/*/episode_{ep:06d}.mp4"]
    return [p for pat in pats for p in root.glob(pat)]


def make_subset(src: Path, dst: Path, episodes: list[int]) -> None:
    meta_src = src / "meta"
    lines = [json.loads(line) for line in (meta_src / "episodes.jsonl").read_text().splitlines() if line.strip()]
    keep = [e for e in lines if e["episode_index"] in set(episodes)]
    if len(keep) != len(set(episodes)):
        raise ValueError(f"episodes {episodes} not all present in {src}")
    (dst / "meta").mkdir(parents=True, exist_ok=True)
    for f in meta_src.iterdir():
        if f.name not in ("episodes.jsonl", "info.json"):
            shutil.copy2(f, dst / "meta" / f.name)
    (dst / "meta" / "episodes.jsonl").write_text("".join(json.dumps(e) + "\n" for e in keep))
    info = json.loads((meta_src / "info.json").read_text())
    info["total_episodes"] = len(keep)
    info["total_frames"] = int(sum(e["length"] for e in keep))
    (dst / "meta" / "info.json").write_text(json.dumps(info, indent=4))
    for ep in episodes:
        files = _episode_files(src, ep)
        if not files:
            raise FileNotFoundError(f"no data/video files for episode {ep} in {src}")
        for f in files:
            target = dst / f.relative_to(src)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, target)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--src", required=True, type=Path)
    ap.add_argument("--out_train", required=True, type=Path)
    ap.add_argument("--out_val", required=True, type=Path)
    ap.add_argument("--val_episodes", type=int, nargs="+", required=True)
    a = ap.parse_args()
    all_eps = [json.loads(line)["episode_index"] for line in (a.src / "meta" / "episodes.jsonl").read_text().splitlines() if line.strip()]
    train = [e for e in all_eps if e not in a.val_episodes]
    make_subset(a.src, a.out_train, train)
    make_subset(a.src, a.out_val, a.val_episodes)
    print(f"train episodes {train} -> {a.out_train}\nval episodes {a.val_episodes} -> {a.out_val}")


if __name__ == "__main__":
    main()
