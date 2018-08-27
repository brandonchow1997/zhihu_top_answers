import requests
import time

'https://www.zhihu.com/topic/19577498/top-answers'
def get_answer(page):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/69.0.3497.12 Safari/537.36'
    }
    topic_id = '19763198'
    base_url = 'https://www.zhihu.com/api/v4/topics/{topic}/feeds/essence?include=data%5B%3F' \
               '%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B' \
               '%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized' \
               '%2Cis_author%2Cvoting' \
               '%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F' \
               '%28target.type%3Danswer%29%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent' \
               '%2Crelevant_info%2Cexcerpt.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F' \
               '%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Darticle%29%5D.target' \
               '.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D' \
               '.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type' \
               '%3Dpeople%29%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed' \
               '%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer' \
               '%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp' \
               '%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.author.badge%5B%3F%28type%3Dbest_answerer%29%5D' \
               '.topics%3Bdata%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cauthor.badge%5B%3F%28type' \
               '%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dquestion%29%5D.target.comment_count' \
               '&limit=10&offset='.format(topic=topic_id)
    url = base_url + str(page * 5)
    # 设置每页显示5个回答
    response = requests.get(url, headers=header)
    return response.json()


# 解析ajax回答
def parse_answer_page(html):
    paging = html['paging']
    is_end = paging['is_end']
    items = html['data']
    for item in items:
        type = item['target']['type']
        id = item['target']['id']
        author_name = item['target']['author']['name']
        author_gender = item['target']['author']['gender']
        author_headline = item['target']['author']['headline']
        answer_content = item['target']['content']

        if type == 'answer':
            question_title = item['target']['question']['title']
            print('问题:', question_title)
            print('回答者:', author_name, end='||')
            print('性别:', author_gender)
            print('回答者简介:', author_headline)
            print('回答id:', id)
            print('-' * 50)
            print(answer_content)
        else:
            article_title = item['target']['title']
            print('专栏文章:', article_title)
            print('作者:', author_name, end='||')
            print('性别:', author_gender)
            print('作者简介:', author_headline)
            print('文章id:', id)
            print('-' * 50)
            print(answer_content)

        print('=' * 60)
        time.sleep(2)
        # comments(id)
    return is_end


##########################################################


def answer():
    i = 0
    while (1):
        i = i + 1
        data = get_answer(i - 1)
        end = parse_answer_page(data)
        time.sleep(2)
        if end == True:
            break


if __name__ == '__main__':
    print('正在爬取：')
    print('杜伦大学')
    print('的精选回答...')
    print('=' * 100)
    print('=' * 100)
    answer()