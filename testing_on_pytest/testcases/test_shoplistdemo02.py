import requests
import pytest

class Test_shoplist(object):

    def test_shoplist(self):
        host = "http://dev-live-assistant.zhiyitech.cn"
        path = "/live-assistant/v1_0/ai-data/live/shop-list"
        params = {
            "endDate": "2021-01-07",
            "newItemFlag": 0,
            "pageNo": 1,
            "pageSize": 20,
            "rankType": 1,
            "rootCategoryId": 80,
            "startDate": "2021-01-07"
        }
        header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "Cookie": "gr_user_id=f268bed5-0042-48bf-afcb-f81915a3a648; grwng_uid=8362e6db-7d48-44d9-bb6c-89bb33f0ffcd; bec8eda69848e602_gr_last_sent_cs1=732413; bec8eda69848e602_gr_cs1=732413",
            "token": "fe4ff0a1 - 6f3e - 4fb7 - b5a1 - f1d3f006f3cc"
        }

        r = requests.request("post",url= host+path,headers = header,data = params)

        print(r.status_code)
        assert  r.status_code == 200

if __name__ == "__main__":
    t1 =  Test_shoplist().test_shoplist()
    pytest.main(["--html=../report/test_shoplist02.html","test_shoplistdemo02.py"])










