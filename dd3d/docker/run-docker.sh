#!/bin/sh

## run the docker container with X11 socket forwarding
MNT_DIR=/dd3d
DOCKER_TAG="towardsautonomy/environments:ubuntu-20.04-cudnn8-cuda-11.3.1-pytorch-1.9.1-dd3d"
# create a xauth file with access permission
xauth nlist $DISPLAY | sed -e 's/^..../ffff/' | xauth -f /tmp/.docker.xauth-n nmerge -
# add non-network local connections to access control list
xhost +local:root
# run docker
sudo docker run -it --rm -e DISPLAY=unix$DISPLAY                     \
                         -v ${PWD}/../:${MNT_DIR}                    \
                         -v /media:/media                            \
			             -v /floppy:/floppy			                 \
                         -v /media:/media                            \
                         -v ${PWD}/../data:/data                     \
                         -v /tmp/.X11-unix:/tmp/.X11-unix            \
                         -v /tmp/.docker.xauth:/tmp/.docker.xauth:rw \
			             -w ${MNT_DIR}				                 \
                         -e PYTHONPATH=${MNT_DIR}                    \
                         -e XAUTHORITY=/tmp/.docker.xauth            \
                         --net=host --ipc host                       \
                         --gpus all $DOCKER_TAG bash
# remove non-network local connections from access control list
xhost -local:root
