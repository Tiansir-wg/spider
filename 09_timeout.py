# coding=utf-8
# 超时和重试机制
import requests
# 需要安装
from retrying import retry


# 最大重试3次
@retry(stop_max_attempt_number=3)
def parse(url):
    # 请求超过3秒则停止
    response = requests.get(url, timeout=3)
    assert response.status_code == 200
    return response.content.decode("utf-8")


if __name__ == '__main__':
    url = "http://www.google.com"
    try:
        html = parse(url)
    except Exception as e:
        print e
        html = None
    print html

