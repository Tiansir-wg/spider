# coding=utf-8
# 使用代理IP
import requests

if __name__ == "__main__":
    proxies = {
        "https": "https://113.66.6.254:808",
        "http": "http://106.111.53.222:9999"
    }

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

    response = requests.get("https://www.baidu.com/", headers=headers, proxies=proxies)
    print(response.status_code)

