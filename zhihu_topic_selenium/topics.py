# topics模块
# author: brandonchow1997

from tqdm import tqdm
import time


# 解析topic页面返回的json数据
def parse_page_json(html_json):
    url_token_list = []
    name_list = []
    data = html_json['payload']
    print('\n'+'--- 已获取关注的话题%s个 ---' % len(data)+'\n')
    pbar = tqdm(data)
    for item in pbar:
        # 设置0.2秒睡眠
        time.sleep(0.2)
        name = item['name']
        pbar.set_description("Processing Topic:%s..." % name)
        url_token = item['url_token']
        url_top_answers = 'https://www.zhihu.com/topic/{url_token}/top-answers'.format(url_token=url_token)
        introduction = item['introduction']
        # 生成topic字典
        print('topic:', name)
        print(introduction)
        print('=' * 80)
        url_token_list.append(url_token)
        name_list.append(name)
        """
        # 存入数据库的代码
        topic_info = {
            'name': name,
            'url_token': url_token,
            'url': url_top_answers,
            'introduction': introduction
        }
        # 存入数据库中
        # save_to_mongo(topic_info)
        # 返回话题的url_token属性和name属性
    # print(url_token_list)
        """
    return len(data), url_token_list, name_list
