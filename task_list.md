# More downstream validations 

## Table of Contents

- [Downstream validation](#validation)
  - [Table of Contents](#table-of-contents)
  - [More datasets](#datasets)
  - [More experiments](#experimenments)
  - [Tasks](#tasks)


## Datasets :fuelpump:
* [x] KITTI
* [ ] KITTI Trackig
* [x] Nuscenes: /s/dat/UserFolders/xzhan258/bevfusion/data/nuscenes
* [ ] Waymo: /s/dat/waymo_open_dataset
* [ ] BDD100k: /s/dat/UserFolders/xzhan258/LaneDetection/BDD100K
* [ ] Culane: /s/dat/UserFolders/xzhan258/LaneDetection/CULane
* [ ] Tusimple: /s/dat/UserFolders/xzhan258/LaneDetection/TuSimple
* [ ] ApolloScape: /s/dat/UserFolders/xzhan258/LaneDetection/ApolloScape
* [ ] Mapillary: /s/dat/UserFolders/xzhan258/LaneDetection/Mapillary

## Experimenments :woman_technologist:
* [x] 3D Object Detection(Cam Only) on Nuscenes
* [x] Monocular 3D Object detection(Cam Only) on KITTI
* [ ] Real-time 3D Object Detection(Lidar) on Waymo 
* [ ] Drivable Area Segmentation(Cam only) on BDD100K

## Tasks :hugs:
* [x] [Data analysis on KITTI](https://github.com/towardsautonomy/DatasetEquity/blob/main/data_analysis/kitti_dataset_distribution_analysis.ipynb)
* [x] [DD3D model training on KITTI](https://github.com/towardsautonomy/dd3d/tree/081a4815565ff4164d50fa06d88e46b23b4c9752)

* [x] [Data analysis on Nuscenes](https://github.com/towardsautonomy/DatasetEquity/blob/downstream-validation-generalize-on-more-datasets/data_analysis/nuscenes_dataset_distribution_analysis.ipynb)
* [x] [BEVFormer model training on NuScenes](https://github.com/towardsautonomy/BEVFormer/tree/2d36d66b1237bec51c68d1f5ab43310adad2a5e1)

* [ ] Data analysis on Waymo
* [ ] CenterNet model training on Waymo

* [ ] Data analysis on BDD100k
* [ ] YOLOP for Drivable Area Segmentation on BDD100K


## Dockers
* [x] YOLOP: harbor.hpc.ford.com/xzhan258/torch:1.10_cuda11.4_yolop
* [x] CenterPoint: harbor.hpc.ford.com/xzhan258/torch:1.10_cuda11.4_centerpoint_waymo
