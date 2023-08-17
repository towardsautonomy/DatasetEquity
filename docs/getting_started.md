# Getting Started

## Installation

Clone the repository and submodules.

```bash
git clone https://github.com/towardsautonomy/DatasetEquity.git --recursive
cd DatasetEquity/BEVFormer
git checkout dataset_equity
cd ..
cd dd3d
git checkout dataset_equity
cd ..
```

Build docker images for `BEVFormer` and `dd3d`.

```bash
cd BEVFormer/docker
sh build-docker.sh
cd ../..
cd dd3d/docker
sh build-docker.sh
cd ../..
```

**Note**: These docker images are already built and available on [Docker Hub](https://hub.docker.com/u/towardsautonomy). You can skip this step if you don't want to build the docker images yourself. Running the docker images will automatically pull the images from Docker Hub.

## Dataset Analysis

Perform dataset analysis on the KITTI dataset by opening up the `data_analysis/kitti_dataset_distribution_analysis.ipynb` notebook, and running the cells. It will generate a file `data_analysis/kitti_training_cluster_info.pkl` which contains all the information needed. By default, this should be copied over to `dd3d/data/datasets/KITTI3D/`.

For the nuScenes dataset, use `data_analysis/nuscenes_dataset_distribution_analysis.ipynb` notebook. It will generate a file `data_analysis/nuscenes_training_cluster_info.pkl`, which should be copied over to `BEVFormer/data/nuscenes/`. These paths can be changed in the project config files.


