#! -*- coding:utf-8 -*-

import time


def set_session_with_expire(request, key, val):
    request.session[key] = val
    request.session[key + '_time'] = int(time.time())
    

def get_session_with_expire(request, key, expire):
    val = request.session.get(key, None)
    val_time = request.session.get(key + '_time', None)

    if not val or not val_time or int(time.time()) - val_time > expire:
        if val:
            del request.session[key]
        if val_time:
            del request.session[key + '_time']
        return None
    return val

def del_session_with_expire(request, key):
    if request.session.get(key, None):
        del request.session[key]
        del request.session[key + '_time']

def get_session_expire(request, key):
    return request.session.get(key + '_time', None)
