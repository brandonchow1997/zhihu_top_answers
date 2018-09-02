# main主函数

import login
import top_answers


if __name__ == '__main__':
    print('-- 请选择 --')
    print('-- 1 Chrome模式 --')
    print('-- 2 无浏览器模式 --')
    choose = input()
    if choose == '1':
        response = login.get_topic()
        url_token = response[1]
        total = response[0]
        top_answers.top_answer(total, url_token)
    if choose == '2':
        response = login.get_topic()
        url_token = response[1]
        total = response[0]
        top_answers.top_answer_opt(total, url_token)