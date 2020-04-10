# coding=utf-8
# 使用selenium选择元素
from selenium import webdriver


if __name__ == '__main__':

    driver = webdriver.Chrome("/Users/sirtian/Documents/environment/chromedriver")

    driver.get("https://movie.douban.com/top250")

    # 根据类名获取元素
    # movie_items = driver.find_elements_by_xpath("//div[@class='item']")

    # 获取文本
    # 注意是find_elements_by_xpath而不是find_element_by_xpath,前者返回列表，后者
    # 返回元素
    # titles = driver.find_elements_by_xpath("//span[@class='title']")
    # for title in titles:
    #     print title.text

    # 获取属性值
    # hrefs = driver.find_elements_by_xpath("//div[@class='hd']/a")
    # for href in hrefs:
    #     print href.get_attribute("href")

    # 选取具有指定文本值的链接
    # next_page_url = driver.find_element_by_link_text("后页>").get_attribute("href")
    # print(next_page_url)

    # 选取包含指定文本值的链接
    # 点击下一页按钮之后需要等待页面加载完后再获取元素,否则会出现获取不到元素的情况
    next_page_url = driver.find_element_by_partial_link_text("后页").get_attribute("href")
    print(next_page_url)

