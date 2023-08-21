Build the docker using the following command:

```bash
cd bevfusion/docker && docker build . -t bevfusion
```

We can then run the docker with the following command:

```bash
nvidia-docker run -it -v `pwd`/../data:/dataset --shm-size 16g bevfusion /bin/bash
```
Then clone the bevfusion submodule and install it:

```bash
cd home && git clone https://github.com/alchemz/bevfusion && cd bevfusion
python setup.py develop
```

You can then create a symbolic link `data` to the `/dataset` directory in the docker.

### Data Preparation

#### nuScenes

Please follow the instructions from [here](https://github.com/open-mmlab/mmdetection3d/blob/master/docs/en/datasets/nuscenes_det.md) to download and preprocess the nuScenes dataset. Please remember to download both detection dataset and the map extension (for BEV map segmentation). After data preparation, you will be able to see the following directory structure (as is indicated in mmdetection3d):

```
mmdetection3d
├── mmdet3d
├── tools
├── configs
├── data
│   ├── nuscenes
│   │   ├── maps
│   │   ├── samples
│   │   ├── sweeps
│   │   ├── v1.0-test
|   |   ├── v1.0-trainval
│   │   ├── nuscenes_database
│   │   ├── nuscenes_infos_train.pkl
│   │   ├── nuscenes_infos_val.pkl
│   │   ├── nuscenes_infos_test.pkl
│   │   ├── nuscenes_dbinfos_train.pkl
```
### Training

To train the camera-only variant for object detection with cbgs dataset, please run:

```bash
torchpack dist-run -np 8 python tools/train.py configs/nuscenes/det/centerhead/lssfpn/camera/256x704/swint/default.yaml --model.encoders.camera.backbone.init_cfg.checkpoint pretrained/swint-nuimages-pretrained.pth
```

To train the camera-only variant for object detection without cbgs dataset, please set ```type``` to ```NoCBGSDataset```  [here](https://github.com/alchemz/bevfusion/blob/d08fd86cccefdacc0f19669cf6c3176a1a51d491/configs/nuscenes/default.yaml#L266). Use the same command as above to train the model.

Use ```dequity_eta``` and ```dequity_gamma``` parameters in [config](https://github.com/alchemz/bevfusion/blob/main/configs/nuscenes/det/centerhead/default.yaml) to change data equity configurations for performing experiments.
