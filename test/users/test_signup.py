#! -*- coding:utf-8 -*-

from basetest import BaseTest
import requests
class TestSignup(BaseTest):


    def test_signup(self):

        action = self.action + '/user/api/signup/'
        data = dict(phone = '12345678901',
                    nick_name = 'testname',
                    password = 'testpass')
        
        conn = self._request('POST', action, data)
        print conn.json()

    
    def test_get_verify_code(self):
        action = self.action + '/user/api/get_verify_code'
        conn = self._request('POST', action)
        print conn


if __name__ == '__main__':
#    TestSignup().test_signup()
    TestSignup().test_get_verify_code()
