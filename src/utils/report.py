"""Collect the numbers produced by the notebooks into one markdown table + figures (results/)."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from .video_metrics import load_scores, paired_comparison, summarize  # noqa: E402


def video_section(res: Path, runs: list[str]) -> tuple[list[str], dict]:
    scores = {r: load_scores(res / f"video_scores_{r}.json") for r in runs}
    lines = ["| run | n | PSNR (dB) | SSIM |", "|---|---|---|---|"]
    summ = {}
    for r, s in scores.items():
        m = summarize(s)
        summ[r] = m
        lines.append(f"| {r} | {m['n']} | {m['psnr_mean']:.2f} ± {m['psnr_std']:.2f} | {m['ssim_mean']:.3f} ± {m['ssim_std']:.3f} |")
    if len(runs) >= 2:
        base, tuned = runs[0], runs[1]
        for metric in ("psnr", "ssim"):
            c = paired_comparison(scores[base], scores[tuned], metric)
            summ[f"paired_{metric}"] = c
            lines.append(f"\nPaired {tuned} − {base} ({metric.upper()}): mean {c['mean_diff']:+.4f}, "
                         f"95% bootstrap CI [{c['ci95'][0]:+.4f}, {c['ci95'][1]:+.4f}], "
                         f"{tuned} better on {c['win_rate']:.0%} of {c['n']} videos")
        fig, ax = plt.subplots(1, 2, figsize=(9, 3.4))
        for a, metric in zip(ax, ("psnr", "ssim")):
            names = sorted({x.name for x in scores[base]} & {x.name for x in scores[tuned]})
            b = {x.name: getattr(x, metric) for x in scores[base]}
            t = {x.name: getattr(x, metric) for x in scores[tuned]}
            a.scatter([b[n] for n in names], [t[n] for n in names])
            lo, hi = min(min(b.values()), min(t.values())), max(max(b.values()), max(t.values()))
            a.plot([lo, hi], [lo, hi], "k--", lw=1)
            a.set_xlabel(f"{base} {metric.upper()}"); a.set_ylabel(f"{tuned} {metric.upper()}")
            a.set_title(f"per-video {metric.upper()} (above line = {tuned} better)", fontsize=8)
        fig.tight_layout(); fig.savefig(res / "video_metrics_scatter.png", dpi=150)
    return lines, summ


def idm_section(res: Path) -> list[str]:
    p = res / "idm_eval.json"
    if not p.exists():
        return []
    d = json.loads(p.read_text())
    lines = [f"\nIDM action error on held-out episodes {d['episodes']} ({d['steps']} steps)\n",
             "| predictor | MSE | MAE | normalised MSE |", "|---|---|---|---|"]
    for k in ("idm", "mean_action", "state_hold"):
        if k in d:
            lines.append(f"| {k} | {d[k]['mse']:.5f} | {d[k]['mae']:.5f} | {d[k]['nmse']:.4f} |")
    return lines


def bench_section(res: Path) -> list[str]:
    lines = []
    for f in sorted(res.glob("dreamgenbench_*.csv")):
        rows = list(csv.DictReader(open(f)))
        lines.append(f"\n`{f.name}`: {len(rows)} rows, columns {list(rows[0].keys()) if rows else []}")
    return lines


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--results", type=Path, default=Path("results"))
    ap.add_argument("--runs", nargs="+", default=["base", "lora"])
    a = ap.parse_args()
    lines = ["# Results (auto-generated from files in results/)\n"]
    if all((a.results / f"video_scores_{r}.json").exists() for r in a.runs):
        v, summ = video_section(a.results, a.runs)
        lines += ["## Cosmos-Predict2 Video2World: generated vs ground-truth video\n", *v]
        (a.results / "video_summary.json").write_text(json.dumps(summ, indent=2))
    lines += idm_section(a.results) + bench_section(a.results)
    (a.results / "summary.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
