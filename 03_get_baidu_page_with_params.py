# coding=utf-8
# 使用request发送带参数的请求
import requests
if __name__ == "__main__":
    wd = raw_input("输入搜索词:")
    # 参数
    params = {'wd': wd}
    # 请求头
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

    # 带参数的get请求
    response = requests.get("https://www.baidu.com/s", params=params, headers=headers)

    print response.content.decode("utf-8")
    print response.request.headers
    print response.headers
    print response.request.url
    print response.url