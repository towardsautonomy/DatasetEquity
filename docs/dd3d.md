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