# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 17:38:10 2020
@author: He Zhuangfa/PCE
"""
from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize

# 去掉停用词函数定义
def remove_stop_words(f):
	stop_words = ['Market']
	for stop_word in stop_words:
		f = f.replace(stop_word, '')
	return f

# 生成词云函数定义
def create_word_cloud(f):
	print('根据词频，开始生成词云，请等待...')
	f = remove_stop_words(f)
	cut_text = word_tokenize(f)
	#print(cut_text)
	cut_text = " ".join(cut_text)
	wc = WordCloud(max_words=100,width=2000,height=1200)
	wordcloud = wc.generate(cut_text)
	# 写词云图片
	wordcloud.to_file("markect_wordcloud.jpg")
	# 显示词云文件
	plt.imshow(wordcloud) #绘制图片
	plt.axis("off") # 消除坐标轴
	plt.show() #显示图片

# 数据加载
data = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
#print(data.shape)

# 读取并处理数据
transactions = []
for i in range(0, data.shape[0]):
	temp = []
	for j in range(0,data.shape[1]):
		item = str(data.values[i,j])
		if item != 'nan':
			temp.append(item)
	transactions.append(temp)
#print(transactions)

# 生成词云
# 用列表解析式将列表转成空格分隔的字符串，'%s' %item表示：将item值插入到%s占位符的字符串中
all_word = ' '.join('%s' %item for item in transactions)
create_word_cloud(all_word)