# -*- coding:utf-8 -*-
'''
创建一些演示数据做测试，导入数据库
'''
from untitled2.wsgi import *
from news.models import Column,Article
def main():
    colums_urls = [
        ('体育新闻','sports'),
        ('社会新闻','society'),
        ('科技新闻','tech'),
    ]
    for colums_name,url in colums_urls:
        c = Column.objects.get_or_create(name = colums_name,slug=url)[0]
        #创建十篇新闻
        for i in range(1,11):
            article = Article.objects.get_or_create(
                title = '{}_{}'.format(colums_name,i),
                slug = 'article_{}'.format(i),
                content = '新闻内容:{}{}'.format(colums_name,i)

            )[0]
            article.column.add(c)
if __name__ == '__main__':
    main()
    print("done")