# https://www.zhihu.com/followed_topics?offset=20&limit=80
import requests
import pymongo


# 利用cookie模拟登录知乎，请求topic页面
def login_zhihu_ajax():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/69.0.3497.12 Safari/537.36 '
    }
    # 传入cookie
    cookies = {
        # 我的账号的cookie
        'z_c0': '"2|1:0|10:1535377292|4:z_c0|92'
                ':Mi4xbnRXSEFnQUFBQUFBVUtjcUNEcnFEU1lBQUFCZ0FsVk5qRTF4WEFBRjZReDBqM1VXOFdRZGxSTVlDMkVYNWNJUjZB'
                '|aee4668c213220b1dce5a3225aa9c3759a0f43d61389c449faa57e3886f752fb" '
    }
    # 显示80个关注的topic（参数limit改变数量）
    url = "https://www.zhihu.com/followed_topics?offset=0&limit=80"
    response = requests.get(url, headers=headers, cookies=cookies)
    return response.json()


# 解析topic页面返回的json数据
def parse_page_json(html_json):
    data = html_json['payload']
    for item in data:
        url_token = item['url_token']
        url_top_answers = 'https://www.zhihu.com/topic/{url_token}/top-answers'.format(url_token=url_token)
        name = item['name']
        introduction = item['introduction']
        topic_info = {
            'name': name,
            'url': url_top_answers,
            'introduction': introduction
        }
        # 生成topic字典
        print('页面链接id:', url_top_answers)
        print('topic:', name)
        print(introduction)
        print('=' * 80)
        # 存入数据库中
        # save_to_mongo(topic_info)
        return url_token


"""
# 连接到MongoDB
MONGO_URL = 'localhost'
MONGO_DB = 'zhihu_topic'
MONGO_COLLECTION = 'topic_info'
client = pymongo.MongoClient(MONGO_URL, port=27017)
db = client[MONGO_DB]


# 存储到数据库
def save_to_mongo(data):
    # 保存到MongoDB中
    try:
        if db[MONGO_COLLECTION].insert(data):
            print('存储到 MongoDB 成功')
    except Exception:
        print('存储到 MongoDB 失败')
"""


#######################################################
# 获取topic
def get_topic():
    # 爬取ajax异步传输的内容
    html_json = login_zhihu_ajax()
    # 解析json
    url_answers = parse_page_json(html_json)
    return url_answers
#######################################################


if __name__ == '__main__':
    get_topic()
