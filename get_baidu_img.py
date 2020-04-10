# coding=utf-8
# 下载百度首页的图片并保存到本地
import requests
import os
if __name__ == "__main__":
    img_url = "https://www.baidu.com/img/dong_d7ee3105570f1673ecf33f5bf2f58c35.gif"
    response = requests.get(img_url)
    # 截取图片名称
    img_name = os.path.split(img_url)[1]
    # 保存为文件
    with open(img_name, "wb") as fi:
        fi.write(response.content)