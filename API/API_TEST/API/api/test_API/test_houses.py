#!encoding = utf-8
from parameterized import param
from parameterized import parameterized
from common import request
from nose.tools import assert_equal
from nose.tools import assert_dict_contains_subset


class test_houses():

    def __init__(self):
        self.url = "http://118.178.113.90/csh/api/houses"
        #self.url = "http://10.10.10.115:80/csh/api/houses"

    def setup(self):
        # print("my class set up")
        pass

    def teardown(self):
        pass

    @parameterized.expand([
        param('{"cityEnName": "cd"}')
    ])
    def test_getHousesOK(self, param):
        print("my param is : "+param)
        r = request.Request().get(self.url, param)
        print(r)
        assert_equal(r['code'], 200)
        assert_equal(r['message'], 'success')
        # assert
        # assert_in(r['data'], 'type')
        # assert_in(r['data'], 'floor')

    @parameterized.expand([
        param('{"cityEnName": "123"}'),
        param('{"cityEnName": "#@$%"}'),
        param('{"cityEnName": "   "}'),
        param('{"cityEnName": 123}'),
        param('{"cityEnName": "select"}'),
        param('{"cityEnName": "select", "name":1234}'),
    ])
    def test_getHousesWithWrongParam(self, param):
        print("my param is :"+param)
        r = request.Request().get(self.url, param)
        assert_equal(r['code'], 200)
        assert_equal(r['message'], 'success')
        assert_equal(r['data'], [])
        assert_equal(r['more'], False)

    @parameterized.expand([
        param('{"cityEnName": ""}'),

    ])
    def test_getHouseWithoutParamValue(self, param):
        print("my param is :"+param)
        r = request.Request().get(self.url, param)
        print(r)
        assert_equal(r['code'], 200)
        assert_equal(r['message'], 'success')
        assert_equal(r['data'], [])
        assert_equal(r['more'], False)