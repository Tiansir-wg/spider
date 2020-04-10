# coding=utf-8
# 获取新浪首页并保存到本地
import requests
import sys
if __name__ == "__main__":
    # 改变python默认的编码
    reload(sys)
    sys.setdefaultencoding("utf-8")
    sina_url = "https://www.sina.com.cn/"
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 \
                            (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}

    response = requests.get(sina_url, headers=headers)

    # 1. 通过response.encoding = "utf-8"解决中文乱码
    # response.encoding = "utf-8"
    # print response.text

    # 2. 通过response.content.decode("utf-8")解决乱码
    # print response.content.decode("utf-8")

    with open("sina.html", "w") as f:
        f.write(response.content.decode("utf-8"))