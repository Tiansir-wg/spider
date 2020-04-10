# coding=utf-8
# xpath使用
import requests
# 需要安装
from lxml import etree

if __name__ == "__main__":

    url = "https://movie.douban.com/chart"

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3)"
                             " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}

    response = requests.get(url, headers=headers)

    # etree.HTML接受Unicode类型和字节类型
    elements = etree.HTML(response.content)

    # 使用xpath语法获取电影标题,lxml处理的结果是Unicode类型
    item_list = elements.xpath("//tr[@class='item']")
    for item in item_list:
        dic = dict()
        dic['title'] = item.xpath("./td/a[@class='nbg']/@title")[0]

        # 之所以要判断是为了防止出现空值
        dic['rating_nums'] = item.xpath("descendant::span[@class='rating_nums']/text()")[0] if len(
            item.xpath("descendant::span[@class='rating_nums']/text()")) > 0 else None

        # 直接打印字典会显示中文的Unicode编码,可以使用json.dumps转化为字符串
        print(u"电影<<{}>>的评分是:{}分".format(dic["title"], dic["rating_nums"]))

    # etree能够将不完整的HTML补全
    # print etree.tostring(elements)


