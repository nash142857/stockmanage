#! -*- coding:utf-8 -*-

from django.http import HttpResponse
import sys,os,math,time,logging,json
import hashlib
import json

def message(msg, code):
    return json.dumps(dict(message = msg, code = code))


def baseresponse(msg, code):
    return HttpResponse(message(msg, code))


def encode_utf8(value): 
    if isinstance(value, unicode):
        return value.encode('utf8')
    return value

def decode_utf8(value):
    if isinstance(value, str):
        return value.decode('utf8')
    return value

def encrypt(string):
    crypt = hashlib.sha256()
    crypt.update(string)
    return crypt.hexdigest()
