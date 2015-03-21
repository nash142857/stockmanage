#!/bin/env python
# coding=utf-8
#     File Name: utils.py
#     Author: Gu Shenlong
#     Mail: blackhero98@gmail.com
#     Created Time: 六  3/21 17:47:40 2015


import sys,os,math,time,logging,json
import hashlib

from madmin import config

def connect_field(string_arr):
    return config.AUTH_SPLIT_FIELD.join(string_arr)

def split_field(string):
    return string.split(config.AUTH_SPLIT_FIELD)
