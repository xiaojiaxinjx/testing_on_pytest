# -*-coding:utf-8-*-
import requests


class Test_douban(object):

    def test_douban(self):
        """https://m.douban.com/j/puppy/frodo_landing?include=anony_home"""
        host = "https://m.douban.com"
        path = "/j/puppy/frodo_landing?include=anony_home"
        header = {
           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
        }

        r = requests.request("GET",url= host+path,headers = header,verify = False)
        response = r.json()

        """
        返回值内容：
        {"data":{"anony_home":{"version":"6.0","banner":{"url":"https://img9.doubanio.com\/view\/puppy_image\/raw\/public\/16ad990ec23uwn790d4.jpg","width":1382,"height":600},"shire_nav_tips":false,"title":"豆瓣"}},"is_preview":false}
        """

        assert r.status_code == 200
        assert r.raise_for_status() ==  None
        assert len(response["data"]) > 0

        print(r.status_code)
        print(r.headers)
        print(r.encoding)
        print(r.text)







