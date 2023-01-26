#!/bin/sh

WORKSPACE="/workspace"
DOCKER_TAG="towardsautonomy/environments:ubuntu-20.04-cudnn8-cuda-11.3.1-pytorch-1.9.1-bevformer"
sudo docker build \
    --build-arg WORKSPACE=$WORKSPACE \
    -f Dockerfile \
    -t $DOCKER_TAG \
    .