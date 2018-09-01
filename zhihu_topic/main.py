import zhihu_topic_answer


# 主函数
if __name__ == '__main__':
    cookie = '"2|1:0|10:1535771357|4:z_c0|92' \
             ':Mi4xbnRXSEFnQUFBQUFBVUtjcUNEcnFEU1lBQUFCZ0FsVk4zVkIzWEFDS09qQXgxeldwWXFHM1prUVpCaThCSmNJZWxR' \
             '|e3893f57a45d70f7a661be30c0a52b8e8cce82658ee159d3d5d0e45f68b7c506" '
    print('-- 演示版请输入：TEST --')
    print('-- 默认则为完整版 --')
    print('请输入:', end='')
    choose = input()
    if choose == 'TEST':
        zhihu_topic_answer.test(cookie)
    else:
        zhihu_topic_answer.main(cookie)