# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 10:19:38 2020

@author: 12339/Hezhuangfa/PCE
"""

"""
采集大众品牌汽车在网上的报价
数据源：易车网大众品牌汽车http://car.bitauto.com/xuanchegongju/?mid=8
字段包括：名称，最低价格，最高价格，产品图片链接
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def get_content(url):
    # 得到页面的内容
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html = requests.get(url, headers=headers, timeout=10)
    content = html.text
    # 通过content创建BeautifulSoup对象
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    return (soup)

def parse_soup(soup):
    # 获得完整的信息框
    temp = soup.find('div', class_='search-result-list')
    # 提取信息框中需要的信息
    car_name = temp.find_all(class_='cx-name text-hover')
    car_price = temp.find_all(class_='cx-price')
    car_picture = temp.find_all(class_='img')

    # 创建DataFrame,将内容添加至df
    df = pd.DataFrame(columns=['名称', '最低价格（万）', '最高价格（万）', '产品图片链接'])
    for i in range(len(car_name)):
        item = {}
        item['名称'] = car_name[i].text
        price = car_price[i].text
        # 价格暂无时，赋值NaN
        if price == "暂无":
            item['最低价格（万）'] = np.NaN
            item['最高价格（万）'] = np.NaN
        elif '-' in price:
            item['最低价格（万）'] = float(price.split('-')[0])
            item['最高价格（万）'] = float(price.split('-')[1][:-1])
        else:
            item['最低价格（万）'] = float(price[:-1])
            item['最高价格（万）'] = float(price[:-1])
        item['产品图片链接'] = 'http:' + car_picture[i]['src']
        df = df.append(item, ignore_index=True)
    return (df)

page_num = 3  # 定义要爬取3页
result_list = pd.DataFrame()
for i in range(page_num):
    url = 'http://car.bitauto.com/xuanchegongju/?mid=8&page=' + str(i + 1)
    soup = get_content(url)
    result_list = pd.concat([result_list, parse_soup(soup)])  # 将每页获取到的列表进行相加（行数上追加）

result_list = result_list.reset_index(drop=True)
print(result_list)
result_list.to_csv('price_volkswagen.csv', encoding='gbk')
