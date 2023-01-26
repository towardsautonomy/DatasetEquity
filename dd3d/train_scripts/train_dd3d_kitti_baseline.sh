#!/bin/sh

WANDB_HOST="https://api.wandb.ai"
WANDB_ENTITY="3d-object-detection"
export WANDB_ENTITY=$WANDB_ENTITY
# make sure to export WANDB_API_KEY in your environment
# export WANDB_API_KEY=$WANDB_API_KEY

wandb login --host $WANDB_HOST $WANDB_API_KEY
./scripts/train.py +experiments=dd3d_kitti_dla34_dequity \
                    WANDB.NAME="dequity_baseline"