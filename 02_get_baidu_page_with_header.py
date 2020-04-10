# coding=utf-8
# 使用request发送带header的请求
import requests
if __name__ == "__main__":
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

    # 带请求头的get请求
    response = requests.get("http://www.baidu.com", headers=headers)

    print response.content.decode("utf-8")
    print response.request.headers
    print response.headers
    print response.request.url
    print response.url