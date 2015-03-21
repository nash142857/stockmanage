#! -*- coding:utf-8 -*-
from users.models import User
from common import utils as comutils

import re
import hashlib
import logging
from random import randint

def check_signup_valid(request):
    phone = request.get('phone', None)
    nick_name = request.get('nick_name', None)
    password = request.get('password', None)
    
    logging.debug('nick_name: ' + nick_name)
    logging.debug('utf-nick_name: ' + comutils.decode_utf8(nick_name))

    if not phone:
        return False, 'phone is require', 1
    if not nick_name:
        return False, 'nick_name is require', 2
    if not password:
        return False, 'password is require', 3
    if not re.match(r'^\d{11}$', phone):
        return False, 'phone is not valid', 4
    if not re.match(ur'^[\w\d_\u4e00-\u9fa5]{2,20}$', comutils.decode_utf8(nick_name)):
        return False, 'nick_name is not valid', 5
    if not is_password_valid(password):
        return False, 'password is not valid', 6
    if not is_phone_valid(phone):
        return False, 'phone is already existed', 7
    if not is_nick_name_valid(nick_name):
        return False, 'nick_name is already existed', 8
    return True,


def is_phone_valid(phone):
    return len(User.objects.filter(phone = phone)) == 0

def is_nick_name_valid(nick_name):
    return len(User.objects.filter(nick_name = nick_name)) == 0

def is_password_valid(password):
    return 6 <= len(password) <= 20

def encrypt_sha256(string):
    crypt = hashlib.sha256()
    crypt.update(string)
    return crypt.hexdigest()


def get_verify_code(size):
    return ''.join([str(randint(0, 9)) for item in range(0, size)])


###############################################################################

def is_avatar_valid(filepath):
    return True

def is_signature_valid(signature):
    return len(signature) <= 200
