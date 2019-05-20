import requests
import json

class Request:

    def __init__(self):
        self.headers = {"Content-Type": "application/json"}
        self.baseUrl = "http://118.178.113.90/csh/api/"


    def get(self, url, para):
        try:
            para = json.loads(para)
            # print(para)
            # print(type(para))
            r = requests.get(url, params=para, headers=self.headers)
            return r.json()
        except BaseException as e:
            print("error occurs!!")
            print("request error:" + str(e))

    def post(self, url, para):

        try:
            # para = json.dumps(para)
            print(para)
            r = requests.post(url, data=para, headers=self.headers)
            return r.json()
        except BaseException as e:
            print("post error:" + str(e))

    @classmethod
    def delete(self, url, para):
        try:
            para = json.dumps(para)
            r = requests.delete(url, data=para, headers=self.headers)
            return r.json()
        except BaseException as e:
            print("delete error:"+str(e))



if __name__ == "__main__":
    r = Request()
    url = "http://47.92.214.232:8080/login"

   #  para = '{"userName": "test", "password": "123456"}'
   # print(r.post(url, para))

    url = "http://118.178.113.90/csh/api/houses"
    para = '{"cityEnName": "cd"}'
    result = r.get(url, para)
    print(result['data'][0])
    print(type(result['data'][0]))
