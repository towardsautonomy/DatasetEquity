# import clustering method
from sklearn.manifold import TSNE
from sklearn.cluster import DBSCAN
from sklearn import metrics
from tqdm.notebook import tqdm
from PIL import Image

# import torch, cv2 and other dependencies
from torchvision import datasets, transforms
import torch
import torch.nn as nn
from torchvision import transforms
from torchvision.models import resnet101

import os
import cv2
import pickle
import logging
import numpy as np
import pathlib
import matplotlib.pyplot as plt
import math
import time
import argparse

# set random seed
import random
random.seed(33)
np.random.seed(33)

class BDD100kDataset(torch.utils.data.Dataset):
    def __init__(
        self,
        data_root,
        image_set="train",
        transform=transforms.Compose([transforms.Resize((384, 384)),
                                      transforms.ToTensor(),
                                      transforms.Normalize(0.5, 0.5),
                                      ]),
        is_test=False,
        keep_difficult=False,
        label_file=None,
        version='100k',
        split='train'
    ):
        """Dataset for BDD100k data.
        Args:
            data_root: the root of the BDD100k dataset,
        """
        self.data_root = data_root
        self.transform = transform
        self.version = version
        self.split = split
        self.filenames, self.tokens = [], []

        if self.version in ['10k', '100k']:
            self.data_root = os.path.join(self.data_root, self.version, self.split)
        else:
            assert self.version in ['10k','100k']
            print('Please use either 10k samples version or 100k full dataset')

        #pbar = tqdm(enumerate(os.listdir(self.data_root)))
        #for filename in os.listdir(self.data_dir):
        img_list = os.listdir(self.data_root)
        for idx, filename in enumerate(tqdm(img_list)):
            img_path = os.path.join(self.data_root, filename)
            self.filenames.append(img_path)
            self.tokens.append(idx)

        print('Number of data samples in the set: {}'.format(len(self.filenames)))

    # method to get length of data
    def __len__(self):
        return len(self.filenames)

    # method to get a sample
    def __getitem__(self, idx):
        # get image
        image_filename = self.filenames[idx]
        image = Image.open(image_filename).convert('RGB')
        # transform image
        image = self.transform(image)
        # get token
        token = self.tokens[idx]
        # return image
        return {'image': image, 'token': token}



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_root', type=str, help="path to load the data")
    parser.add_argument('--results_dir', type=str, help="folder to save the embeddings")
    parser.add_argument('--feature_extactor', type=str, help="model to extract the embeddings")
    parser.add_argument('--data_type', type=str, help="select 10k or 100k")


    args = parser.parse_args()

    results_dir_timestamp = os.path.join(args.results_dir, time.strftime("%Y%m%d_%H%M%S"))
    if not os.path.exists(results_dir_timestamp):
        os.makedirs(results_dir_timestamp)
        print('INFO: {} created to store retrieval results \n'.format(results_dir_timestamp))

    if args.data_type == 'bdd100k':
        dataset = BDD100kDataset(data_root=args.data_root, version='100k', split='train')
    else:
        pass


    dataset_str='bdd100k'
    train_features_fname = os.path.join(args.results_dir, f'{dataset_str}_training_features.pkl')
    train_cluster_info_fname = os.path.join(args.results_dir, f'{dataset_str}_training_cluster_info.pkl')


    if args.feature_extactor == 'resnet101':
        # use a pre-trained model to get the feature vectors for all the images
        # in the dataset
        model = resnet101(pretrained=True, progress=True)
        # remove the last layer keeping the weights
        model = torch.nn.Sequential(*list(model.children())[:-1])

        model.eval()
        model.cuda()
        train_tokens, train_features = [], []
        with torch.no_grad():
            for i in tqdm(range(len(dataset))):
                img = dataset[i]['image'].unsqueeze(0).cuda()
                # inference
                feature = model(img).flatten().cpu().numpy()
                train_features.append(feature)
                train_tokens.append(dataset[i]['token'])
        train_features = np.array(train_features)
        # save the features to disk as a pickle file
        with open(train_features_fname, 'wb') as f:
            pickle.dump({'tokens': train_tokens, 'features': train_features}, f)
    else:
        pass


