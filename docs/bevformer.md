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