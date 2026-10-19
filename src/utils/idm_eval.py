"""Quantitative evaluation of the *official* GR00T-Dreams inverse-dynamics model.

`IDM_dump/dump_idm_actions.py --output_dir P` writes a copy of dataset G in which the `action`
column holds the IDM's pseudo-actions. Because G still carries ground-truth actions we can measure
how accurate the pseudo-labels are, and compare against two trivial baselines computed from the
training episodes only (mean action; zero-order hold of `observation.state`).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def load_episode_arrays(dataset: Path, column: str = "action") -> dict[int, np.ndarray]:
    """{episode_index: (T, D) float array} from a LeRobot dataset's parquet files."""
    import pandas as pd  # needs pyarrow; present on Colab

    out = {}
    for f in sorted(dataset.glob("data/chunk-*/episode_*.parquet")):
        df = pd.read_parquet(f, columns=[column])
        out[int(f.stem.split("_")[1])] = np.stack(df[column].to_numpy()).astype(np.float64)
    if not out:
        raise FileNotFoundError(f"no parquet episodes under {dataset}/data")
    return out


def read_groups(dataset: Path) -> dict[str, tuple[int, int]]:
    mod = json.loads((dataset / "meta" / "modality.json").read_text())["action"]
    return {k: (v["start"], v["end"]) for k, v in mod.items()}


def action_errors(pred: dict[int, np.ndarray], gt: dict[int, np.ndarray], train_mean: np.ndarray,
                  groups: dict[str, tuple[int, int]], hold: dict[int, np.ndarray] | None = None) -> dict:
    """MSE / MAE / normalised MSE (per-dimension GT variance) for the model and the baselines."""
    eps = sorted(set(pred) & set(gt))
    if not eps:
        raise ValueError("prediction and ground truth share no episode")
    P = np.concatenate([pred[e] for e in eps])
    G = np.concatenate([gt[e] for e in eps])
    if P.shape != G.shape:
        raise ValueError(f"shape mismatch pred {P.shape} vs gt {G.shape}")
    var = np.maximum(G.var(axis=0), 1e-8)
    baselines = {"mean_action": np.broadcast_to(train_mean, G.shape)}
    if hold is not None:
        baselines["state_hold"] = np.concatenate([hold[e][: len(gt[e])] for e in eps])

    def stats(x: np.ndarray) -> dict:
        err = x - G
        res = {"mse": float((err ** 2).mean()), "mae": float(np.abs(err).mean()),
               "nmse": float(((err ** 2).mean(axis=0) / var).mean()), "per_group_mse": {}}
        for name, (s, e) in groups.items():
            res["per_group_mse"][name] = float((err[:, s:e] ** 2).mean())
        return res

    out = {"episodes": eps, "steps": int(len(G)), "idm": stats(P)}
    for k, v in baselines.items():
        out[k] = stats(np.asarray(v))
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--gt", required=True, type=Path, help="held-out LeRobot dataset given to dump_idm_actions.py")
    ap.add_argument("--pred", required=True, type=Path, help="--output_dir of dump_idm_actions.py")
    ap.add_argument("--train", required=True, type=Path, help="training dataset (for the mean-action baseline)")
    ap.add_argument("--out", type=Path, default=Path("results/idm_eval.json"))
    a = ap.parse_args()
    gt, pred = load_episode_arrays(a.gt), load_episode_arrays(a.pred)
    train_mean = np.concatenate(list(load_episode_arrays(a.train).values())).mean(axis=0)
    try:
        state = load_episode_arrays(a.gt, "observation.state")
    except Exception:  # column missing: skip that baseline
        state = None
    res = action_errors(pred, gt, train_mean, read_groups(a.gt), state)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(res, indent=2))
    for k in ("idm", "mean_action", "state_hold"):
        if k in res:
            print(f"{k:12s} mse={res[k]['mse']:.5f} mae={res[k]['mae']:.5f} nmse={res[k]['nmse']:.4f}")


if __name__ == "__main__":
    main()
