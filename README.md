# zhihu_top_answers
爬取用户所关注的所有话题下的全部精选回答，包括回答者/作者，简介，性别，具体内容。
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
根据不同话题，创建不同的txt文件，将内容分类存入
![result](https://github.com/brandonchow1997/zhihu_top_answers/blob/master/result.png)
