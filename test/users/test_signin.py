#! -*- coding:utf-8 -*-

from basetest import BaseTest
import requests
class TestSignup(BaseTest):


    def test_signin(self):

        action = self.action + '/user/api/signin/'
        data = dict(phone = '12345678901',
                    password = '123456')
        
        conn = self._request('POST', action, data)
        print conn.json()
        
        ## test correct
        data = dict(phone = '12345678910',
                    password = '123456')
        
        conn = self._request('POST', action, data)
        print conn.json()['message']

    

if __name__ == '__main__':
    TestSignup().test_signin()
