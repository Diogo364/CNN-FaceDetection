# -*- coding: utf-8 -*-
# @Author: Diogo Telheiro do Nascimento
# @Date:   2022-03-20 18:17:58
# @Last Modified by:   Diogo Telheiro do Nascimento
# @Last Modified time: 2022-03-20 19:28:05

import numpy as np
import tensorflow as tf

class Yolov3:
    def __init__(self):
        self._model = tf.keras.Sequential([
            
        ])
    
    @classmethod
    def build_from_cfg_file(cls, path):
        layers = []
        curr_layer = {}
        with open(path, 'r') as cfg:
            for line in cfg:
                if line[0] == '[':
                    layer_type 


