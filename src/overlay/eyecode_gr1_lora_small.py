"""Small-scale LoRA post-training experiment for the *official* cosmos-predict2 repo.

Copied by notebook 01 into `cosmos_predict2/configs/base/experiment/`, where the repo's own
`config.py` auto-registers every module of that package. Nothing is re-implemented here: it only
re-uses the repo's `Dataset`, model config and LoRA switches with a reduced budget.

Environment knobs (read at import time so they can be set from the notebook):
  EYECODE_DATASET_DIR  folder with videos/ metas/ t5_xxl/   (default datasets/eyecode_gr1_train)
  EYECODE_MAX_ITER     number of optimiser steps             (default 300)
  EYECODE_SAVE_ITER    checkpoint interval                   (default 100)
  EYECODE_NUM_WORKERS  dataloader workers                    (default 2)
"""
import os

from hydra.core.config_store import ConfigStore
from megatron.core import parallel_state
from torch.utils.data import DataLoader, DistributedSampler

from cosmos_predict2.data.dataset_video import Dataset
from imaginaire.lazy_config import LazyCall as L

DATASET_DIR = os.environ.get("EYECODE_DATASET_DIR", "datasets/eyecode_gr1_train")
MAX_ITER = int(os.environ.get("EYECODE_MAX_ITER", "300"))
SAVE_ITER = int(os.environ.get("EYECODE_SAVE_ITER", "100"))
NUM_WORKERS = int(os.environ.get("EYECODE_NUM_WORKERS", "2"))
NUM_FRAMES = int(os.environ.get("EYECODE_NUM_FRAMES", "13"))
VIDEO_H = int(os.environ.get("EYECODE_VIDEO_H", "224"))
VIDEO_W = int(os.environ.get("EYECODE_VIDEO_W", "400"))
assert (NUM_FRAMES - 1) % 4 == 0 and VIDEO_H % 16 == 0 and VIDEO_W % 16 == 0
STATE_T = (NUM_FRAMES - 1) // 4 + 1


def get_sampler(dataset):
    return DistributedSampler(
        dataset,
        num_replicas=parallel_state.get_data_parallel_world_size(),
        rank=parallel_state.get_data_parallel_rank(),
        shuffle=True,
        seed=0,
    )


# _dataset = L(Dataset)(dataset_dir=DATASET_DIR, num_frames=NUM_FRAMES, video_size=(VIDEO_H, VIDEO_W))  # same as official groot.py
_dataset = L(Dataset)(dataset_dir=DATASET_DIR, num_frames=NUM_FRAMES, video_size=(VIDEO_H, VIDEO_W))
_dataloader = L(DataLoader)(
    dataset=_dataset,
    sampler=L(get_sampler)(dataset=_dataset),
    batch_size=1,
    drop_last=True,
    num_workers=NUM_WORKERS,
    pin_memory=True,
)

cs = ConfigStore.instance()
cs.store(group="dataloader_train", package="dataloader_train", name="eyecode_gr1_small", node=_dataloader)

predict2_video2world_lora_eyecode_gr1_small = dict(
    defaults=[
        {"override /model": "predict2_video2world_fsdp_2b"},
        {"override /optimizer": "fusedadamw"},
        {"override /scheduler": "lambdalinear"},
        {"override /ckpt_type": "standard"},
        {"override /dataloader_val": "mock"},
        {"override /dataloader_train": "eyecode_gr1_small"},
        "_self_",
    ],
    job=dict(project="posttraining", group="video2world_lora", name="2b_eyecode_gr1_small"),
    model=dict(
        config=dict(
            train_architecture="lora",
            lora_rank=16,
            lora_alpha=16,
            lora_target_modules="q_proj,k_proj,v_proj,output_proj,mlp.layer1,mlp.layer2",
            init_lora_weights=True,
            pipe_config=dict(
                state_t=STATE_T,
                ema=dict(enabled=False),  # saves memory on a single GPU
                prompt_refiner_config=dict(enabled=False),
                guardrail_config=dict(enabled=False),
            ),
        )
    ),
    model_parallel=dict(context_parallel_size=1),
    trainer=dict(
        distributed_parallelism="fsdp",  # overridden from the command line (ddp / fsdp) by the notebook
        callbacks=dict(iter_speed=dict(hit_thres=10)),
        max_iter=MAX_ITER,
    ),
    checkpoint=dict(save_iter=SAVE_ITER),
    optimizer=dict(lr=2 ** (-14.5), weight_decay=0.2),
    scheduler=dict(warm_up_steps=[0], cycle_lengths=[MAX_ITER], f_max=[0.6], f_min=[0.0]),
)

cs.store(
    group="experiment",
    package="_global_",
    name="predict2_video2world_lora_eyecode_gr1_small",
    node=predict2_video2world_lora_eyecode_gr1_small,
)
