# Are All Samples Created Equal? In The Quest For Equity Within Datasets

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
make docker-build DOCKERFILE=Dockerfile-cu113
cd ../..
```

## Training BEVFormer

Run the docker container in interactive mode.

```bash
cd BEVFormer/docker
sh run-docker.sh
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
...
```
