#!coding=utf-8
import nose
#nose.main()
from nose import with_setup
#nose.run()
from nose.plugins.attrib import attr
from nose.tools import assert_equal, assert_in
from parameterized import parameterized
from parameterized import param
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import common.request


class TestLogin:

    def __init__(self):
        self.url = "http://47.92.214.232:8080/login"
        # baseUrl = "http://118.178.113.90/csh/api/"

    def setup(self):
        print("my class setup")

    # @attr(mode="login successfully")
    @parameterized.expand([

        '{"userName": "test", "password": "123456"}'

    ])
    def test_loginOK(self,param):
        print("the param is :"+param)
        r = common.request.Request().post(self.url, param)
        print(r)
        assert_equal('0', r['code'])
        assert_equal('登录成功', r['msg'])

    @parameterized([
        '{"userName": "test1", "password": "123456"}',
        '{"userName": "123", "password": "123456"}',
        '{"userName": "@#$", "password": "123456"}',
        '{"userName": "None", "password": "123456"}',
        # '{"userName": "中国", "password": "123456"}'
    ])
    def test_loginwithwrongname(self, param):
        print("the param is :" + param)
        r = common.request.Request().post(self.url, param)
        print(r)
        assert_equal('2', r['code'])
        assert_in(None, r.values(), "log in with wrong name test in failed")

    def test_loginwithwrongpassword(self, param):
        print("the param is :" + param)
        r = common.request.Request().post(self.url, param)
        print(r)
        assert_equal('2', r['code'])
        assert_in(None, r.values(), "log in with wrong name test in failed")

    def test_loginwithoutname(self):
        pass

    def test_loginwithoutpassword(self):
        pass


    def teardown(self):
        print("my class tear down")




