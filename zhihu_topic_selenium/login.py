# cookie登录的login模块
# author: brandonchow1997

import requests
import topics


def login_zhihu():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/69.0.3497.12 Safari/537.36 '
    }
    # 传入cookie:'z_c0'
    cookies = {
        # 我的账号的cookie
        'z_c0': '"2|1:0|10:1535779643|4:z_c0|92'
                ':Mi4xbnRXSEFnQUFBQUFBVUtjcUNEcnFEU1lBQUFCZ0FsVk5PM0YzWEFCLUp4bl9sQXBWOFBleDJqV3E1SEJLN1UtWFJB'
                '|331ef4e0fee0c2a208bf9fac16c463e438b303ba583a13986955e01eea56c5a5" '
    }
    # 显示80个关注的topic（参数limit改变数量）
    url = "https://www.zhihu.com/followed_topics?offset=0&limit=80"
    response = requests.get(url, headers=headers, cookies=cookies)
    return response.json()


def get_topic():
    # 爬取ajax异步传输的内容
    html_json = login_zhihu()
    # 解析json
    url_answers = topics.parse_page_json(html_json)
    return url_answers
