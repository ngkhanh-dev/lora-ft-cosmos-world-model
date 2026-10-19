"""Build a small train / held-out split of the official GR1-100 dataset (nvidia/GR1-100).

Layout expected (as produced by the official cosmos-predict2 doc step 1.1):
    <src>/videos/*.mp4 and <src>/metadata.csv   (header line, then `file.mp4,"prompt"`)
Outputs:
    <out_train>/videos/*.mp4 + metadata.csv     -> input of scripts.get_t5_embeddings_from_groot_dataset
    <out_eval>/videos/*.mp4 (ground truth), <out_eval>/frames/*.png (first frame), <out_eval>/batch_input.json
The split is deterministic (seeded), and train/eval never share a video.
"""
from __future__ import annotations

import argparse
import csv
import json
import random
import shutil
from pathlib import Path

import cv2


def read_metadata(csv_path: Path) -> dict[str, str]:
    with open(csv_path, newline="") as fh:
        rows = list(csv.reader(fh))
    return {Path(r[0]).name: r[1].strip() for r in rows[1:] if len(r) >= 2}


def write_metadata(path: Path, items: dict[str, str]) -> None:
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["file_name", "text"])
        for name, prompt in items.items():
            w.writerow([name, prompt])


def first_frame(video: Path, out_png: Path) -> None:
    cap = cv2.VideoCapture(str(video))
    ok, frame = cap.read()
    cap.release()
    if not ok:
        raise RuntimeError(f"cannot decode {video}")
    cv2.imwrite(str(out_png), frame)


def split(names: list[str], n_train: int, n_eval: int, seed: int) -> tuple[list[str], list[str]]:
    if n_train + n_eval > len(names):
        raise ValueError(f"requested {n_train}+{n_eval} videos but only {len(names)} available")
    names = sorted(names)
    random.Random(seed).shuffle(names)
    return sorted(names[:n_train]), sorted(names[n_train:n_train + n_eval])


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--src", required=True, type=Path, help="folder holding videos/ and metadata.csv")
    ap.add_argument("--out_train", required=True, type=Path)
    ap.add_argument("--out_eval", required=True, type=Path)
    ap.add_argument("--n_train", type=int, default=24)
    ap.add_argument("--n_eval", type=int, default=8)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--eval_output_dir", default="output/eval", help="where generated videos will be written")
    ap.add_argument("--prompt_prefix", default="The robot arm is performing a task. ",
                    help="same prefix the official T5 script prepends (inference must use the same text)")
    a = ap.parse_args()

    meta = read_metadata(a.src / "metadata.csv")
    available = [n for n in meta if (a.src / "videos" / n).exists()]
    train, held = split(available, a.n_train, a.n_eval, a.seed)

    for d in (a.out_train / "videos", a.out_eval / "videos", a.out_eval / "frames"):
        d.mkdir(parents=True, exist_ok=True)
    for n in train:
        shutil.copy2(a.src / "videos" / n, a.out_train / "videos" / n)
    write_metadata(a.out_train / "metadata.csv", {n: meta[n] for n in train})

    batch = []
    for n in held:
        shutil.copy2(a.src / "videos" / n, a.out_eval / "videos" / n)
        png = a.out_eval / "frames" / n.replace(".mp4", ".png")
        first_frame(a.src / "videos" / n, png)
        batch.append({"input_video": str(png), "prompt": a.prompt_prefix + meta[n],
                      "output_video": str(Path(a.eval_output_dir) / "{run}" / n)})
    (a.out_eval / "batch_input_template.json").write_text(json.dumps(batch, indent=2))
    (a.out_eval / "split.json").write_text(json.dumps({"train": train, "eval": held, "seed": a.seed}, indent=2))
    print(f"train={len(train)} eval={len(held)} -> {a.out_train}, {a.out_eval}")


if __name__ == "__main__":
    main()
