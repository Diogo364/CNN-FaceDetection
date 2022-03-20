# -*- coding: utf-8 -*-
# @Author: Diogo Telheiro do Nascimento
# @Date:   2022-03-20 19:45:53
# @Last Modified by:   Diogo Telheiro do Nascimento
# @Last Modified time: 2022-03-20 21:14:26

def clean_line(string):
    return string.strip()

def parse_str_to_numeric(string):
    if '.' in string:
        return float(string)
    return int(string)

def extract_numeric_tuples_from_str(string, sep=','):
    return tuple(map(parse_str_to_numeric, string.split(sep)))
