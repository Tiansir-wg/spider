# coding=utf-8
# 使用selenium模拟浏览器
# 需要安装, webdriver需要从淘宝镜像安装,版本号和本机Chrome版本要一致


from selenium import webdriver
import time
if __name__ == '__main__':

    # 实例化driver
    driver = webdriver.Chrome("/Users/sirtian/Documents/environment/chromedriver")

    driver.get("http://www.baidu.com")

    # 在input标签输入内容
    driver.find_element_by_id("kw").send_keys("python")

    # 点击元素
    driver.find_element_by_id("su").click()

    # 获取页面源码
    # print(driver.page_source)

    # cookie
    # print(driver.get_cookies())

    # 当前URL
    # print(driver.current_url)

    # 调整页面大小
    # driver.maximize_window()
    # driver.set_window_size(1080, 980)

    time.sleep(3)
    # 关闭当前页面
    driver.close()

    # 退出浏览器
    # driver.quit()
