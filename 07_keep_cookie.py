# coding=utf-8
# 携带cookie的请求
import requests
import sys

if __name__ == "__main__":

    reload(sys)
    sys.setdefaultencoding("utf-8")

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
    # 实例化session
    session = requests.session()

    # 使用session发送post请求，服务器会把cookie保存在session中
    post_url = "http://www.renren.com/PLogin.do"

    # 登录信息
    post_data = {
        "email": "15872397013",
        "password": "@soledad4454213"
    }

    session.post(post_url, data=post_data, headers=headers)

    # 请求个人主页，
    response = session.get("http://www.renren.com/974186979", headers=headers)

    # 通过看保存的HTML页面中是否有自己的用户判断是否登录成功
    with open("renren.html", "w") as fi:
        fi.write(response.content.decode("utf-8"))

    # 上面是通过session携带cookie的,也可以:
    # 1. 浏览器拷贝cookie字符串放到请求头并传递给get请求的headers参数
    # headers = {"User-Agent":"*","cookies":"*"}
    # request.get(url, headers)
    # 2. 将cookies字符串转化为字典并传递给cookies参数
    # cookie_dict = {i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
    # requests.get(url, headers,cookies=cookie_dict)

    # 获取加密数据方式:1. 观察变化 2. 定位js(通过event listener或搜索URL地址)  3. 分析js(断点)  4. 执行js(python模拟)
