# zhihu_top_answers
爬取用户##使用的是我的cookie，可自行修改cookie值:z_c0##所关注的所有话题下的全部精选回答，包括回答者/作者，简介，性别，具体内容。
库依赖：requests,pymongo
-- 运行main.py即可 --
--------------------
2018.8.27
增加了通过cookie模拟登录知乎后，进入话题页面，获取自己关注的话题的url，title，headline（存入MongoDB中）。
在zhihu_topic_answer.py中引入topic.py模块，根据topic所获取的话题url_token属性，合成完整的url地址，
一次性爬取所有关注话题下所有精选回答。（按类分别爬取）
--------------------
将要实现（选择是否增加获取每一条精选回答下的全部评论。）
-------------------
2018.8.28
爬取话题增加了进度条，并显示当前爬取的话题名称
根据不同话题，分别创建各个话题的txt文件，将内容分类分别存入
-------------------
2018.8.30更新
评论增加所属话题属性，在zhihu_topic_answer.py中引入zhihu_comments模块（增加了评论获取模块）。
在爬取所有话题后，增加（y/s）输入选项，选择是否附加爬取精华回答下的所有评论（并存入MongoDB中，可自行修改）。
##暂时未添加代理池，请注意爬取的速率和时间间隔，防止弹出验证码或者是被封ip##
![result](https://github.com/brandonchow1997/zhihu_top_answers/blob/master/result.png)
