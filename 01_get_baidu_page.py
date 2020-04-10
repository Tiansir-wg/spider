# coding=utf-8
# 使用request发请求并解决中文乱码问题
import requests

if __name__ == "__main__":
    response = requests.get("http://www.baidu.com")
    # response.encoding = "utf-8"
    # response.text返回Unicode解码格式
    # print response.text

    # response.content返回字节类型，还没有解码。
    print response.content.decode("utf-8")

    # 请求头
    print response.request.headers
    # 响应头
    print response.headers
    # 请求URL地址
    print response.request.url
    # 响应URL地址
    print response.url



