# DatasetEquity: Are All Samples Created Equal? In The Quest For Equity Within Datasets

This is the official implementation of the paper: DatasetEquity. This paper proposes a novel method to ensure dataset equity by weighing each sample differently in the training process according to its likelihood of occurrence within the dataset. This simple and intuitive approach boosts the performance of current state-of-the-art 3D object detection methods towards a higher NDS and mAP score.

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

## Training BEVFormer

Run the docker container in interactive mode.

```bash
cd BEVFormer/docker
sh run-docker.sh
```

Prepare the pre-trained model.

```bash
cd BEVFormer
mkdir ckpts

cd ckpts & wget https://github.com/zhiqi-li/storage/releases/download/v1.0/r101_dcn_fcos3d_pretrain.pth
```

Prepare the nuScenes dataset.

Download `Full dataset (v1.0)` and `CAN bus expansion` from [here](https://www.nuscenes.org/download) and unzip.

```bash
mkdir data
cd data
# create symlink to the dataset
ln -s /path/to/nuScenes/data/sets/nuscenes nuscenes
# create symlink to the CAN bus data
ln -s /path/to/nuScenes/data/sets/can_bus can_bus
cd ..
# prepare dataset
python tools/create_data.py nuscenes --root-path ./data/nuscenes --out-dir ./data/nuscenes --extra-tag nuscenes --version v1.0 --canbus ./data
# You should see the following structure
BEVFormer
├── projects/
├── tools/
├── configs/
├── ckpts/
│   ├── r101_dcn_fcos3d_pretrain.pth
├── data/
│   ├── can_bus/
│   ├── nuscenes/
│   │   ├── maps/
│   │   ├── samples/
│   │   ├── sweeps/
│   │   ├── v1.0-test/
|   |   ├── v1.0-trainval/
|   |   ├── nuscenes_infos_temporal_train.pkl
|   |   ├── nuscenes_infos_temporal_val.pkl
```

Train the baseline model (`variants={base|small|tiny}`).

```bash
python tools/train.py projects/configs/bevformer/bevformer_{variant}.py --deterministic
```

If using a launcher for distributed training, use the following command.

```bash
python tools/train.py projects/configs/bevformer/bevformer_{variant}.py --deterministic --launcher pytorch
```

For training the model with dataset equity configurations, first change the parameters `model.pts_bbox_head.dequity_eta` and `model.pts_bbox_head.dequity_gamma` in the config file (`projects/configs/bevformer/bevformer_{variant}_de.py`) to the desired values.

```bash
python tools/train.py projects/configs/bevformer/bevformer_{variant}_de.py --deterministic --launcher pytorch
```

## Training DD3D

Prepare KITTI dataset.

```bash
mkdir -p data/datasets/KITTI3D
cd data/datasets/KITTI3D
# make symlinks to the KITTI dataset
ln -s /path/to/kitti/training training
ln -s /path/to/kitti/testing testing
# download a standard splits subset of KITTI
curl -s https://tri-ml-public.s3.amazonaws.com/github/dd3d/mv3d_kitti_splits.tar | sudo tar xv -C ./
cd ../../../..
```

Run the docker container in interactive mode.

```bash
cd dd3d/docker
sh run-docker.sh
```

Train the model with various dequity loss configs.
```bash
./train_scripts/train_dd3d_kitti_{dequity_config}.sh
```

Options for `dequity_config` are:
```bash
baseline
eta0.3_gamma2.0
eta0.5_gamma5.0
... etc.
```

For more information specific to `BEVFormer` and `dd3d`, please refer to their respective repositories.
