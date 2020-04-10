# coding=utf-8
# 获取cookie值
import requests

if __name__ == "__main__":

    # 将verify置为False就不会检查ssl证书错误(ssl.CertificateError)
    response = requests.get("http://www.baidu.com", verify=False)

    # RequestsCookieJar类型
    print type(response.cookies)

    # 转化为字典
    cookies = requests.utils.dict_from_cookiejar(response.cookies)
    print(cookies)