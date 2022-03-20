# -*- coding: utf-8 -*-
# @Author: Diogo Telheiro do Nascimento
# @Date:   2022-03-20 18:17:58
# @Last Modified by:   Diogo Telheiro do Nascimento
# @Last Modified time: 2022-03-20 21:27:17

import argparse
import tensorflow as tf
import utils

class LayersConfigExtractor:
    def __init__(self, path):
        self._path = path
        self.__layers = []
        self.__layer_names = []
    
    def __get_layer_name_from_line(self, line):
        return line[1:-1]
    
    def __get_layer_parameter_from_line(self, line):
        return map(utils.clean_line, line.split('='))
    
    @staticmethod
    def __get_activation_function(value):
        if value == 'linear':
            return tf.keras.activations.linear
        elif value == 'leaky':
            tf.nn.leaky_relu
        
    def __clean_anchors(self, value):
        str_tuples = value.split(',  ')
        return list(map(utils.extract_numeric_tuples_from_str, str_tuples))
    
    def __clean_parameter_values(self, parameter, value):
        if parameter == 'activation':
            return self.__get_activation_function(value)
        elif parameter == 'anchors':
            return self.__clean_anchors(value)
        elif ',' in value:
            return utils.extract_numeric_tuples_from_str(value)
        try:
            value = utils.parse_str_to_numeric(value)
        except ValueError:
            pass
        return value

    def layers(self):
        return self.__layers
    
    def layer_names(self):
        return self.__layer_names

    def extract_layers(self):
        curr_attributes = {}
        with open(self._path, 'r') as cfg:
            for line in cfg:
                line = utils.clean_line(line)
                if len(line) > 0:
                    first_char = line[0]
                    if first_char == '#':
                        continue
                    if first_char == '[':
                        if len(curr_attributes) > 0:
                            self.__layers.append(curr_attributes)
                            curr_attributes = {}
                        layer_type = self.__get_layer_name_from_line(line)
                        self.__layer_names.append(layer_type)
                        curr_attributes[layer_type] = {}
                    else:
                        parameter, value = self.__get_layer_parameter_from_line(line)
                        value = self.__clean_parameter_values(parameter, value)
                        curr_attributes[layer_type][parameter] = value
            else:
                self.__layers.append(curr_attributes)
        return self.layers()

if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('-p', '--path', type=str, required=True,
                        help='Path to Network Architecture config file.')    
    args = parse.parse_args()

    extractor = LayersConfigExtractor(args.path)
    layers = extractor.extract_layers()

    for idx, layer in enumerate(extractor.layer_names(), start=1):
        print(f'{idx}: {layer}')
    

