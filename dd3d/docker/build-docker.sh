#!/bin/sh

WORKSPACE="/workspace"
DOCKER_TAG="towardsautonomy/environments:ubuntu-20.04-cudnn8-cuda-11.3.1-pytorch-1.9.1-dd3d"
sudo docker build \
    --build-arg WORKSPACE=$WORKSPACE \
    -f Dockerfile-cu113 \
    -t $DOCKER_TAG \
    .