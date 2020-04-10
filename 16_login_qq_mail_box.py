# coding=utf-8
from selenium import webdriver
import time
# selenium模拟登陆QQ邮箱
# 登录表单在iframe中,需要进行iframe切换


if __name__ == '__main__':

    url = "https://mail.qq.com"

    driver = webdriver.Chrome("/Users/sirtian/Documents/environment/chromedriver")

    driver.get(url)

    # 切换到iframe
    driver.switch_to.frame("login_frame")

    # 邮箱,密码
    driver.find_element_by_id('u').send_keys("12***1800@qq.com")
    driver.find_element_by_id('p').send_keys('@******')

    # 点击登录
    driver.find_element_by_id('login_button').click()

    time.sleep(4)

    driver.quit()




