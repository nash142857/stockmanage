from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from users.models import User
from users.config import SIGNUP_VERIFY_CODE_EXPIRE, UPLOAD_AVATAR_DIR
from users import utils as userutils
from common import utils as comutils
from common import httputils as comhttps
from common import modelutils as commodels

import os
import time
from uuid import uuid4
import logging




@csrf_exempt
def signup(request):

    if request.method != 'POST':
        raise Http404

    validation = userutils.check_signup_valid(request.POST)
    if not validation[0]:
        return comutils.baseresponse(validation[1], validation[2])
       
    phone = request.POST.get('phone')
    nick_name = request.POST.get('nick_name')
    password = request.POST.get('password')

    user = User(phone = phone,
                nick_name = nick_name,
                password = userutils.encrypt_sha256(password))
    try:
        user.save()
    except Exception, e:
        logging.error(e)
        return comutils.baseresponse('system error', 10)
    
    request.session['pk'] = user.pk
    request.session['is_login'] = True
    request.session['phone'] = phone
    request.session['nick_name'] = nick_name

    return comutils.baseresponse('succ', 0)


###############################################################################

@csrf_exempt
def set_verify(request):
    
    if request.method != 'POST':
        raise Http404

    if not request.session.get('is_login', None):
        return comutils.baseresponse('must sigin first', 1)
    
    is_verify = comhttps.get_session_with_expire(request, 'is_verify', SIGNUP_VERIFY_CODE_EXPIRE)
    if not is_verify:
        return comutils.baseresponse('must verify first', 2)

    phone = request.POST.get('phone', None)
    nick_name = request.POST.get('nick_name', None)

    if request.session['phone'] != phone or request.session['nick_name'] != nick_name:
        return comutils.baseresponse('phone or nickname not match', 3)

    try:
        User.objects.filter(pk = request.session['pk']).update(is_verify = True)
    except:
        return comutils.baseresponse('system error', 4)
    comhttps.del_session_with_expire(request, 'is_verify')

    return comutils.baseresponse('set_verify success', 0)


###############################################################################



@csrf_exempt
def reset_password(request):
    
    if request.method != 'POST':
        raise Http404

    if not request.session.get('is_login', None):
        return comutils.baseresponse('must sigin first', 1)

    is_verify = comhttps.get_session_with_expire(request, 'is_verify', SIGNUP_VERIFY_CODE_EXPIRE)
    if not is_verify:
        return comutils.baseresponse('must verify first', 2)

    passwd = request.POST.get('password', None)
    confirm_passwd = request.POST.get('confirm_passwd', None)
    if not passwd or not confirm_passwd:
        return comutils.baseresponse('password is require', 3)

    if passwd != confirm_passwd:
        return comutils.baseresponse('password no match', 4)
    
    if not userutils.is_password_valid(passwd):
        return comutils.baseresponse('password is not valid', 5)

    try:
        User.objects.filter(pk = request.session['pk']).update(password = userutils.encrypt_sha256(passwd))
    except:
        return comutils.baseresponse('system error', 6)
    comhttps.del_session_with_expire(request, 'is_verify')

    return comutils.baseresponse('reset password success', 0)

###############################################################################


@csrf_exempt
def upload_avatar(request):
    
    if request.method != 'POST':
        raise Http404

    if not request.session.get('is_login', None):
        return comutils.baseresponse('must sigin first', 1)

    upload_file = request.FILES.get('upload_avatar', None)
    if not upload_file:
        return comutils.baseresponse('avatar can not be empty', 1)

#    name, ext = os.path.splitext(os.path.basename(upload_file.name))
    filename = str(uuid4())
    filepath = os.path.join(UPLOAD_AVATAR_DIR, filename)
    with open(filepath, 'wb') as myfile:
        myfile.write(upload_file.read())
    
    if not userutils.is_avatar_valid(filepath):
        os.remove(filepath)
        return comutils.baseresponse('avatar is not valid', 2)
    
    try:
        user = User.objects.get(pk = request.session['pk'])
        if not user.avatar:
            user.avatar = filename
            user.save()
        else:
            avatar = os.path.join(UPLOAD_AVATAR_DIR, user.avatar)
            if os.path.isfile(avatar):
                os.remove(avatar)
            os.rename(filepath, avatar)
    except Exception, e:
        logging.error(e)
        logging.error('get avatar error')
        return comutils.baseresponse('system error', 3)
    
    return comutils.baseresponse('upload avatar success', 0)


###############################################################################



@csrf_exempt
def set_signature(request):
    
    if request.method != 'POST':
        raise Http404

    if not request.session.get('is_login', None):
        return comutils.baseresponse('must sigin first', 1)

    signature = request.POST.get('signature', None)
    if not signature:
        return comutils.baseresponse('signature can not be empty', 1)
    if not userutils.is_signature_valid(signature):
        return comutils.baseresponse('signature is not valid', 2)

    try:
        User.objects.filter(pk = request.session['pk']).update(signature = signature)
    except:
        return comutils.baseresponse('system error', 3)

    return comutils.baseresponse('set signature success', 0)


###############################################################################

@csrf_exempt
def get_verify_code(request):

    if request.method != 'POST':
        raise Http404

    ## check sign up or login
    if not request.session.get('is_login', None):
        return comutils.baseresponse('must signin first', 1)

#    last_time = request.session.get('verify_time', None)
    last_time = comhttps.get_session_expire(request, 'verify_code')
    if last_time and int(time.time()) - last_time < SIGNUP_VERIFY_CODE_EXPIRE:
        return comutils.baseresponse('already send', 0)

    verify_code = userutils.get_verify_code(6)
    logging.debug('verify_code: ' + verify_code)

    ## send message
    ## if ret:
    ## else


#    request.session['verify_code'] = verify_code
#    request.session['verify_time'] = int(time.time())
        
    comhttps.set_session_with_expire(request, 'verify_code', verify_code)

    return comutils.baseresponse('get verify code success', 0)


###############################################################################



@csrf_exempt
def check_verify_code(request):
    
    if request.method != 'POST':
        raise Http404

    ## check login
    if not request.session.get('is_login', None):
        return comutils.baseresponse('must signin first', 1)

#    verify_code = request.session.get('verify_code', None)
#    last_time = request.session.get('verify_time', None)
#    if not verify_code or not last_time or int(time.time()) - last_time > SIGNUP_VERIFY_CODE_EXPIRE:
#        if verify_code:
#            del request.session['verify_code']
#        if verify_time:
#            del request.session['verify_time']
#        return comutils.baseresponse('fail: verify code is expire', 1)
    verify_code = comhttps.get_session_with_expire(request, 'verify_code', SIGNUP_VERIFY_CODE_EXPIRE)
    if not verify_code:
        return comutils.baseresponse('verify code is expire', 1)

    post_code = request.POST.get('verify_code', None)
    if not post_code or verify_code != post_code:
        return comutils.baseresponse('fail: verify code error', 2)

    logging.debug('post_code: ' + post_code)
    
#    try:
#        User.objects.filter(pk = request.session['pk']).update(is_verify = True)
#    except:
#        return comutils.baseresponse('fail: system error', 3)
    
#    del request.session['verify_time']
#    del request.session['verify_code']
    comhttps.del_session_with_expire(request, 'verify_code')

#    reqeust.session['is_verify'] = True
#    reqeust.session['is_verify_time'] = int(time.time())
    comhttps.set_session_with_expire(request, 'is_verify', True)

    return comutils.baseresponse('check verify code success', 0)
  

###############################################################################

@csrf_exempt
def signin(request):

    if request.method != 'POST':
        raise Http404
    
    phone = request.POST.get('phone', None)
    password = request.POST.get('password', None)

    if not phone or not password:
        return comutils.baseresponse('phone or email can not be empty', 1)
    
    try:
#        user = User.objects.get(phone = phone)
        user = commodels.get_object_or_none(User, phone = phone)
    except Exception, e:
        logging.error(e)
        return comutils.baseresponse('system error', 4)

    if not user:
        return comutils.baseresponse('user not found', 2)
    if userutils.encrypt_sha256(password) != user.password:
        return comutils.baseresponse('password is not correct', 3)

    request.session['is_login'] = True
    request.session['pk'] = user.pk
    request.session['phone'] = user.phone
    request.session['nick_name'] = user.nick_name
    
    return comutils.baseresponse(str(user), 0)


###############################################################################

@csrf_exempt
def signout(request):

    if request.method != 'POST':
        raise Http404

    request.session.flush()
    return comutils.baseresponse('signout success', 0) 


###############################################################################

def check_login(request):
    
    is_login = request.session.get('is_login', None)
    pk = request.session.get('pk', None)

    return comutils.baseresponse(str(is_login) + ' ' + str(pk), 0)



