# coding=utf-8
# 使用request模拟百度翻译
import requests
import json
import sys


class Fanyi:
    def __init__(self, query_string):
        self.url = "https://fanyi.baidu.com/basetrans"
        self.query_string = query_string
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Mobile Safari/537.36",
            "cookie": open("cookie.txt", "r").readlines()[0],
            "token": "2808d7036878ffa1130432556f714c00",
            "sign": "232427.485594"
        }

    def get_post_data(self):
        post_data = {"query": self.query_string, "from": "zh", "to": "en"}
        return post_data

    def parse_url(self, data):
        response = requests.post(self.url, data=data, headers=self.headers)
        return response.content.decode("utf-8")

    def get_ret(self, json_str):
        obj = json.loads(json_str)
        ret = obj["trans"][0]["dst"]
        return ret

    def run(self):
        # 1.URL地址，data
        post_data = self.get_post_data()
        # 2.发送请求,获取响应
        json_string = self.parse_url(post_data)
        # 3.提取数据
        print("{}翻译结果是:{}".format(self.query_string, json_string))


if __name__ == "__main__":
    initial = raw_input()
    fanyi = Fanyi(initial)
    fanyi.run()

