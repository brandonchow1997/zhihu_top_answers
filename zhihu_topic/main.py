import zhihu_topic_answer


# 主函数
if __name__ == '__main__':
    print('-- 演示版请输入：TEST --')
    print('-- 默认则为完整版 --')
    choose = input()
    if choose == 'TEST':
        zhihu_topic_answer.test()
    else:
        zhihu_topic_answer.main()