# coding=utf-8
import requests
from lxml import etree
from queue import Queue
import time
import threading
# 多线程抓取糗事百科段子


class QiuShiBaiKe:

    # 初始化请求头和临时地址
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) '
                                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.'
                                      '163 Safari/537.36'}
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_list_queue = Queue()

    # 初始化URL
    def init_urls(self):
        base_url = "https://www.qiushibaike.com/text/page/{}"
        for i in range(13):
            self.url_queue.put(base_url.format(i+1))

    # 解析URL
    def parse_url(self):
        while True:
            url = self.url_queue.get()
            response = requests.get(url, headers=self.headers, timeout=3)
            print response
            if response.status_code != 200:
                self.url_queue.put(url)
            # 保存响应界面
            self.html_queue.put(response.content)
            # get和task_done一起使用才能让队列计数减1
            self.url_queue.task_done()

    # 获取内容
    def get_content_list(self):
        while True:
            html_str = self.html_queue.get()
            html_ele = etree.HTML(html_str)
            div_list = html_ele.xpath("//div[@class='col1 old-style-col1']/div")
            content_list = []
            for div in div_list:
                item = dict()
                item["user_name"] = div.xpath(".//h2/text()")[0].strip()
                line = [li.strip() for li in div.xpath(".//div[@class='content']/span/text()")]
                item["joke"] = "".join(line)
                content_list.append(item)

            self.content_list_queue.put(content_list)
            self.html_queue.task_done()

    def save(self):
        while True:
            content_list = self.content_list_queue.get()
            # for content in content_list:
            #     print(u"{}的段子:{}\n".format(content['user_name'].strip(), content['joke']))
            pass
        self.content_list_queue.task_done()

    def run(self):

        # 线程列表
        thread_list = []

        # 准备URL的线程,注意target这里的函数名不能带括号,否则就不是以线程方式执行
        t_url = threading.Thread(target=self.init_urls)
        thread_list.append(t_url)

        # 发起请求的线程
        for t in range(3):
            t_parse = threading.Thread(target=self.parse_url)
            thread_list.append(t_parse)

        # 获取数据的线程
        t_c = threading.Thread(target=self.get_content_list)
        thread_list.append(t_c)

        # 保存数据的线程
        t_s = threading.Thread(target=self.save)
        thread_list.append(t_s)

        for t in thread_list:

            # 子线程设置为守护线程,线程执行函数都是死循环,所以需要设置为守护线程
            # 当主线程执行完毕后退出
            t.setDaemon(True)
            t.start()

        # 阻塞当前线程,直到所有队列的任务都执行完毕
        for q in [self.content_list_queue, self.url_queue, self.html_queue]:
            q.join()


if __name__ == '__main__':
    start_time = time.time()
    qiubai = QiuShiBaiKe()
    qiubai.run()
    print(u"总时间是:{}s".format(time.time() - start_time))
