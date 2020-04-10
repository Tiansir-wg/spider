# coding=utf-8
import requests
from lxml import etree
# 不同之处,使用JoinableQueue和Process，其他地方基本是一致的
from multiprocessing import JoinableQueue
from multiprocessing import Process
import time
from retrying import retry
# 多进程抓取糗事百科段子


class QiuShiBaiKe:

    # 初始化请求头和临时地址
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) '
                                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.'
                                      '163 Safari/537.36'}
        self.url_queue = JoinableQueue()
        self.html_queue = JoinableQueue()
        self.content_list_queue = JoinableQueue()

    # 初始化URL
    def init_urls(self):
        base_url = "https://www.qiushibaike.com/text/page/{}"
        for i in range(13):
            self.url_queue.put(base_url.format(i+1))

    # 解析URL
    @retry(stop_max_attempt_number=3)
    def parse_url(self):
        while True:
            url = self.url_queue.get()
            response = requests.get(url, headers=self.headers, timeout=3)
            print response
            if response.status_code != 200:
                self.url_queue.put(url)
            # 保存响应界面
            self.html_queue.put(response.content)
            # 让队列计数减1
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

        # 进程列表
        process_list = []

        # 准备URL的进程,注意target这里的函数名不能带括号,否则就不是以进程方式执行
        t_url = Process(target=self.init_urls)
        process_list.append(t_url)

        # 发起请求的进程
        for process in range(3):
            t_parse = Process(target=self.parse_url)
            process_list.append(t_parse)

        # 获取数据的进程
        t_c = Process(target=self.get_content_list)
        process_list.append(t_c)

        # 保存数据的进程
        t_s = Process(target=self.save)
        process_list.append(t_s)

        for process in process_list:

            # 子进程设置为守护进程,进程执行函数都是死循环,所以需要设置为守护进程
            # 当主进程执行完毕后退出
            process.daemon = True
            process.start()

        # 阻塞当前进程,直到所有队列的任务都执行完毕
        for q in [self.content_list_queue, self.url_queue, self.html_queue]:
            q.join()


if __name__ == '__main__':
    start_time = time.time()
    qiubai = QiuShiBaiKe()
    qiubai.run()
    print(u"总时间是:{}s".format(time.time() - start_time))
