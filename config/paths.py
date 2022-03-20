# -*- coding: utf-8 -*-
# @Author: Diogo Telheiro do Nascimento
# @Date:   2022-03-20 18:09:03
# @Last Modified by:   Diogo Telheiro do Nascimento
# @Last Modified time: 2022-03-20 18:16:06
import os
from os import path as osp

WORKSPACE_PATH = '/workspace'
model_path = osp.join(WORKSPACE_PATH, 'model')
resources_path = osp.join(WORKSPACE_PATH, 'resources')

DATASET_PATH = '/dataset'
widerface_dataset_path = osp.join(DATASET_PATH, 'WiderFace')