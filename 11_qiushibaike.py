# coding=utf-8
import requests
from lxml import etree
import time
# 抓取糗事百科段子

class QiuShiBaiKe:

    # 初始化请求头和临时地址
    def __init__(self):
        self.temp_url = "https://www.qiushibaike.com/text{}"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) '
                                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.'
                                      '163 Safari/537.36'}

    # 解析URL
    def parse_url(self, page):
        # 下一页处的链接形式是 /text/page/2,需要将/text去掉
        response = requests.get(self.temp_url.format(page[5:]), headers=self.headers)
        return response.content

    # 获取内容
    def get_content_list(self, html_str):
        html_ele = etree.HTML(html_str)
        div_list = html_ele.xpath("//div[@class='col1 old-style-col1']/div")
        content_list = []
        for div in div_list:
            item = dict()
            item["user_name"] = div.xpath(".//h2/text()")[0].strip()
            line = [li.strip() for li in div.xpath(".//div[@class='content']/span/text()")]
            item["joke"] = "".join(line)
            content_list.append(item)

        # 下一页链接
        next_page = html_ele.xpath("//a[child::span[@class='next']]/@href")
        if len(next_page) > 0:
            next_page = next_page[0]
        return next_page, content_list

    def save(self, content_list):
        for content in content_list:
            print(u"{}的段子:{}\n".format(content['user_name'].strip(), content['joke']))

    def run(self):
        # 1.准备初始URL
        page = '/text'
        count = 0
        while len(page) > 0:
            print(u"第{}页".format(count + 1))
            # 2.发送请求，获取响应
            html = self.parse_url(page)
            # 3.提取信息
            page, content_list = self.get_content_list(html)
            # 4.保存
            self.save(content_list)
            count += 1


if __name__ == '__main__':
    start_time = time.time()
    qiubai = QiuShiBaiKe()
    qiubai.run()
    print(u'总时间是:{}s'.format(time.time() - start_time))