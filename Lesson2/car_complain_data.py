# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 09:31:35 2020
@author: He Zhuangfa/PCE

Action1：汽车投诉信息采集：
数据源：http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-1.sHTML
投诉编号，投诉品牌，投诉车系，投诉车型，问题简述，典型问题，投诉时间，投诉状态
可以采用Python爬虫，或者第三方可视化工具
"""

from bs4 import BeautifulSoup
import pandas as pd
import requests

#从URL中获取HTML文档
def request_URL(URL):
    r=requests.get(URL)
    if r.status_code!=200: #状态码为 200 表示请求成功
        raise Exception() #触发异常
    HTML_doc=r.text
    soup = BeautifulSoup(HTML_doc,features="lxml") # BeautifulSoup的解析器
    return soup

#从HTML文档解析得到需求的字符串，并写入到列表
def parse_soup(soup):        
    str = soup.find("div",class_="tslb_b")
    tr_list = str.find_all('tr')[1:] #第0行为标题行，不需要它
    tablelist=[]
    for line in tr_list:
        tdlist=line.find_all('td') #在某行中，不同的列的值存在td标签下
        rowlist=[]
        for i in tdlist:
            rowlist.append(i.text) #只获取其显示文本     
        tablelist.append(rowlist)
    return tablelist

page_num=30 #定义要爬取30页
resultlist=[]
for i in range(page_num):
    URL='http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-' + str(i+1) + '.sHTML'#URL地址累加
    soup = request_URL(URL)
    resultlist=resultlist+parse_soup(soup) #将每页获取到的列表进行相加（行数上追加）

df = pd.DataFrame(resultlist,columns=['id','brand','car_model','type','desc','problem','datetime','status'])
df.to_csv("C:/Users/86180/Desktop/Python练习/SVW Data Engine/Lesson2/car_complain_data.csv",encoding="gbk")