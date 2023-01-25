export BDD100K_DIR=/s/dat/UserFolders/xzhan258/LaneDetection/BDD100K/bdd100k_images/bdd100k/images
export OUT_DIR=/s/dat/UserFolders/xzhan258/private_dev/DatasetEquity/data_analysis/bdd100k
export ROOT=/s/dat/UserFolders/xzhan258/private_dev/DatasetEquity/data_analysis

python $ROOT/feature_extraction.py \
--data_root $BDD100K_DIR \
--results_dir $OUT_DIR \
--feature_extactor resnet101 \
--data_type bdd100k


# cd /s/dat/UserFolders/xzhan258/private_dev/DatasetEquity/data_analysis && runpytorch -J feature_extraction -NGPUS 1 -i harbor.hpc.ford.com/xzhan258/torch:1.10_cuda11.4_yolop -x launcher.sh
