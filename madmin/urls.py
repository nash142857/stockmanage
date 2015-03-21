#!/bin/env python
# coding=utf-8
#     File Name: madmin/urls.py
#     Author: Gu Shenlong
#     Mail: blackhero98@gmail.com
#     Created Time: Sat 21 Mar 2015 08:25:52 PM CST


import sys,os,math,time,logging,json
from django.conf.urls import patterns, include, url
from madmin import views 
urlpatterns = patterns('',
    url(r'login/$',views.login,name='admin_login'),
    url(r'logout/$',views.logout,name='admin_out'),
    url(r'check_auth/$',views.check_auth,name='admin_check_auth'),
    url(r'get_users_trade/$',views.get_users_trade,name='admin_get_users_trade'),
)


