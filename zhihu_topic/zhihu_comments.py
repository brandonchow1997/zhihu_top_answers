# 问题：如何看待温州乐清 20 岁女生乘坐滴滴顺风车遇害 ？是否反应出客服系统存在问题？
import requests
import pymongo


##########################################################
def get_comments(id, page):
    try:
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/69.0.3497.12 Safari/537.36'
        }

        url = 'https://www.zhihu.com/api/v4/answers/{id}/comments?include=data%5B*%5D.author%2Ccollapsed' \
            '%2Creply_to_author%2Cdisliked%2Ccontent%2Cvoting%2Cvote_count%2Cis_parent_author%2Cis_author' \
            '%2Calgorithm_right&order=normal&limit=20&offset='.format(id=id) + str(page * 20) + '&status=open'
        response = requests.get(url, headers=header)
        return response.json()
    except Exception:
        print('get_comments() failed...')


# 解析函数
def parse_comments(html, topic_name):
    try:
        items = html['data']
        is_end = html['paging']['is_end']
        for item in items:
            name = item['author']['member']['name']
            gender = item['author']['member']['gender']
            comment = item['content']
            vote_count = item['vote_count']
            print(name, end='||')
            print(gender)
            print(comment)
            print('赞同数:', vote_count)
            print('-' * 60)
            info = {
                'topic': topic_name,
                'name': name,
                'gender': gender,
                'comment': comment,
                'vote_count': vote_count
            }
            save_to_mongo(info)
            return is_end
    except Exception:
        print('parse_comments() failed...')


# 存储到数据库
def save_to_mongo(data):
    # 保存到MongoDB中
    try:
        if db[MONGO_COLLECTION].insert(data):
            print('存储到 MongoDB 成功')
    except Exception:
        print('存储到 MongoDB 失败')


# 连接到MongoDB
MONGO_URL = 'localhost'
MONGO_DB = 'zhihu_topic'
MONGO_COLLECTION = 'topic_comments'
client = pymongo.MongoClient(MONGO_URL, port=27017)
db = client[MONGO_DB]


##########################################################
# 引用函数
def comments(id, topic_name):
    page = 0
    print('-- 正在爬取评论 --')
    print('...')
    while True:
        page = page + 1
        # 每页爬取20条评论
        html = get_comments(id, page - 1)
        is_end = parse_comments(html, topic_name)
        if is_end is True:
            break
##########################################################
