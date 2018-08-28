import requests
import time
# 引入topic.py
import topics


def get_answer(page, keyword):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/69.0.3497.12 Safari/537.36'
    }
    topic_id = '{topic}'.format(topic=keyword)
    # base_url
    base_url = 'https://www.zhihu.com/api/v4/topics/{topic}/feeds/essence?'.format(topic=topic_id) \
               + 'include=data%5B%3F(target.type%3Dtopic_sticky_module)%5D.target.data%5B%3F(' \
                 'target.type%3Danswer)%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting' \
                 '%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F(target.type%3Dtopic_sticky_module)%5D.target.data%5B%3F(' \
                 'target.type%3Danswer)%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info' \
                 '%2Cexcerpt.author.badge%5B%3F(type%3Dbest_answerer)%5D.topics%3Bdata%5B%3F(' \
                 'target.type%3Dtopic_sticky_module)%5D.target.data%5B%3F(' \
                 'target.type%3Darticle)%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B' \
                 '%3F(type%3Dbest_answerer)%5D.topics%3Bdata%5B%3F(' \
                 'target.type%3Dtopic_sticky_module)%5D.target.data%5B%3F(' \
                 'target.type%3Dpeople)%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count' \
                 '%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics%3Bdata%5B%3F(' \
                 'target.type%3Danswer)%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting' \
                 '%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F(target.type%3Danswer)%5D.target.author.badge%5B%3F(' \
                 'type%3Dbest_answerer)%5D.topics%3Bdata%5B%3F(' \
                 'target.type%3Darticle)%5D.target.content%2Cauthor.badge%5B%3F(' \
                 'type%3Dbest_answerer)%5D.topics%3Bdata%5B%3F(target.type%3Dquestion)%5D.target.comment_count' \
               + '&offset='
    url = base_url + str(page * 5) + '&limit=5'
    # 设置每页显示5个回答
    response = requests.get(url, headers=header)
    # print(response.text)
    return response.json()


# 解析ajax回答
def parse_answer_page(html):
    paging = html['paging']
    is_end = paging['is_end']
    items = html['data']
    try:
        for item in items:
            type = item['target']['type']
            # id = item['target']['id']
            author_name = item['target']['author']['name']
            author_gender = item['target']['author']['gender']
            author_headline = item['target']['author']['headline']
            comment_count = item['target']['comment_count']
            content = item['target']['content']
            if type == 'answer':
                question_title = item['target']['question']['title']
                # content = item['target']['content']
                print('问题:', question_title)
                print('回答者:', author_name, end='||')
                print('性别:', author_gender)
                print('回答者简介:', author_headline)
                # print('回答id:', id)
                print('评论数:', comment_count)
                print(content)
                print('-' * 50)

            else:
                article_title = item['target']['title']
                content = item['target']['content']
                print('专栏文章:', article_title)
                print('作者:', author_name, end='||')
                print('性别:', author_gender)
                print('作者简介:', author_headline)
                # print('文章id:', id)
                print('评论数:', comment_count)
                print(content)
                print('-' * 50)

            print('=' * 60)
            time.sleep(2)
    except Exception:
        print('crawel failed')
        # comments(id)
    return is_end


##########################################################
def answer(keyword):
    i = 0
    while (1):
        i = i + 1
        data = get_answer(i - 1, keyword)
        end = parse_answer_page(data)
        time.sleep(2)
        if end == True:
            break


#######################################################


if __name__ == '__main__':
    # ####从topics模块，获取topics##### #
    keyword = topics.get_topic()
    # ####从topics模块，获取topics##### #
    # keyword[1]为话题的name属性
    print('正在爬取')
    print('--', keyword[1], '--')
    print('的精选回答...')
    time.sleep(2)
    print('=' * 100)
    print('=' * 100)
    # keyword[0]为话题的url_token属性
    answer(keyword[0])
