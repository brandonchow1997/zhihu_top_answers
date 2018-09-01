# main主函数

import login
import top_answers


if __name__ == '__main__':
    response = login.get_topic()
    url_token = response[1]
    total = response[0]
    top_answers.top_answer(total, url_token)