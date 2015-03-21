#! coding:utf-8 -*-

import requests

class BaseTest(object):

    def __init__(self):
        self.action = 'http://localhost'
        self.cookies = {}
        self.header = {
        'Connection':'keep-alive',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'}


    def _request(self, method, action, data = None):
        if method == 'POST':
            conn = requests.post(action, data = data, headers = self.header, cookies = self.cookies)
        if method == 'GET':
            conn = requests.get(action, params = data, headers = self.header, cookies = self.cookies)
        conn.encoding = 'utf-8'
        return conn

    def _print_cookies(self, cookie):
        for key, val in cookie.items():
            print key, ' = ', val
