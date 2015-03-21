from django.shortcuts import render

from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from madmin import utils as madminutils
from common import utils as comutils
from common import httputils as comhttps
from common import modelutils as commodels
from madmin.models import Madmin
import logging
@csrf_exempt
def login(request):
    if request.method != "POST":
        raise Http404
    adminname = request.POST.get("adminname", None)
    passwd = request.POST.get("passwd", None)
   
    if not adminname or not passwd:
        return comutils.baseresponse("adminname or passwd is None", 1)
    
    # check database
    try:
        admin  = commodels.get_object_or_none(Madmin, adminname = adminname)
    except Exception as e:
        logging.error("find adminname:{0} internal error: {1}".format(adminname, e))
        return comutils.baseresponse("internal error", 4)

    #check admin
    if not admin:
        return comutils.baseresponse("admin not found", 2)

    #check passwd
    if comutils.encrypt(passwd) != admin.passwd:
        return comutils.baseresponse("passwd it not correct", 3)

    request.session["is_login"] = True
    request.session["pk"] = admin.pk
    request.session["adminname"] = admin.adminname
    #record authority
    request.session["authority"] = admin.authority
    logging.debug("admin login success:{0}".format(admin.adminname))
    return comutils.baseresponse("admin login success", 0)

@csrf_exempt
def logout(request):
    if request.method != "POST":
        raise Http404

    #flush session
    request.session.flush()
    return comutils.baseresponse("logout success",0)

@csrf_exempt
def check_auth(request):
    if request.method != "POST":
        raise Http404

    auth_field = request.POST.get("auth_field", None)
    #post auth  
    if not auth_field:
        return comutils.baseresponse("no include auth_field", 1)
   
    login_status = request.session.get("is_login",None)
    #check login
    if not login_status:
        return comutils.baseresponse("login in first", 2)

    #get author list
    authority = request.session.get("authority",None)
    if not authority:
        return comutils.baseresponse("no authority list found", 3)

    auth_list =  madminutils.split_field(authority)
    
    #check auth
    if auth_field not in auth_list:
        return comutils.baseresponse("don't have authority for this field", 4)


    #succced
    return comutils.baseresponse("check success",0)

# get user_trade db to get user trade information
@csrf_exempt
def get_users_trade(request):
    return comutils.baseresponse("not developed interface", 1)


# update user_voucher_db to send voucher
@csrf_exempt
def send_voucher(request):
    return comutils.baseresponse("not developed interface", 1)



#TODO
'''
    require: 6-12
'''
