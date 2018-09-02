# selenium实现的top_answers模块
# author: brandonchow1997

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from lxml import etree


def top_answer(total, url_token):
    # 声明浏览器对象初始化
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, 10)

    for i in range(1, total):
        url_top_answers = 'https://www.zhihu.com/topic/{url_token}/top-answers'.format(url_token=url_token[i-1])
        browser.get(url_top_answers)
        get_answer_url(browser)
        time.sleep(2)


def top_answer_opt(total, url_token):
    # 创建chrome参数对象
    opt = webdriver.ChromeOptions()
    opt.set_headless()

    # 创建chrome无界面对象
    browser = webdriver.Chrome(options=opt)
    wait = WebDriverWait(browser, 10)
    for i in range(1, total):
        url_top_answers = 'https://www.zhihu.com/topic/{url_token}/top-answers'.format(url_token=url_token[i-1])
        browser.get(url_top_answers)
        get_answer_url(browser)
        time.sleep(2)


def get_answer_url(browser):
    html = browser.page_source
    data = etree.HTML(html)
    items = data.xpath('//*[@id="TopicMain"]/div[3]/div/div/div')
    for item in items:
        try:
            url_content = item.xpath('./div/meta[3]/@content')
            print('=' * 60)
            print(url_content[0])
            answer_content(url_content[0], browser)
        except Exception:
            pass


def answer_content(url, browser):
    try:
        browser.get(url)
        html = browser.page_source
        data = etree.HTML(html)
        ################################
        question = data.xpath('//*[@id="root"]/div/main/div/div[1]/div[2]/div[1]/div[1]/h1/text()')
        answerer = data.xpath('//*[@id="root"]/div/main/div/div[2]/div[1]/div[2]/div/div/div[1]/div[1]/div/div[1]/span/div/div/a/text()')
        answerer_info = data.xpath('//*[@id="root"]/div/main/div/div[2]/div[1]/div[2]/div/div/div[1]/div[1]/div/div[2]/div/div/text()')
        vote = data.xpath('//*[@id="root"]/div/main/div/div[2]/div[1]/div[2]/div/div/div[1]/div[2]/span/button/text()')
        comments = data.xpath('//*[@id="root"]/div/main/div/div[2]/div[1]/div[2]/div/div/div[2]/div[3]/div[1]/button[1]/text()')
        contents = data.xpath('//*[@class="RichText ztext CopyrightRichText-richText"]/child::text()')
        ################################
        for que in question:
            print(que)
        for ans in answerer:
            print(ans, end='||')
        for ans_info in answerer_info:
            print(ans_info)
        for vote_num in vote:
            print(vote_num)
        for com in comments:
            print(com)
        print('-' * 60)
        try:
            for content in contents:
                print(content)
        except Exception:
            print('Content Error')
            pass
        ################################
    except Exception as e:
        print('Error', e.args)
        pass




