# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 20:12:55 2020

@author: 12339/He Zhuangfa_PCE
"""

from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

#数据加载，选取5个核心车辆对比数据
data = pd.read_csv("CarPrice_Assignment.csv", encoding="gbk")
train_x = data[["fueltype","doornumber","carbody","wheelbase","price"]]
#print(train_x)

# 使用LabelEncoder将字段中的文本类型转化为数字
labels = ["fueltype","doornumber","carbody","wheelbase","price"]
for label in labels:
    train_x[label] = LabelEncoder().fit_transform(train_x[label])
#print(train_x[label])

#将数据使用Min_max方法规范到[0,1]区间
min_max_scaler = preprocessing.MinMaxScaler()
train_x = min_max_scaler.fit_transform(train_x)
#print(train_x)

#KMeans手肘法，选取最优K值
sse = []
for k in range(1,11):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(train_x)
    # 计算inertia簇内误差平方和
    sse.append(kmeans.inertia_)
x = range(1,11)
plt.xlabel("K")
plt.ylabel("SSE")
plt.plot(x,sse,"o-")
plt.show()

#使用KMeans算法进行聚类，由手肘法可知，K值取为4
kmeans = KMeans(n_clusters=4)
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)
#print(predict_y)

#合并聚类结果并插入到原数据中
result = pd.concat((data, pd.DataFrame(predict_y)),axis=1)
result.rename({0:u"聚类结果"}, axis=1, inplace=True)
print(result)
result.to_csv("car_cluster.csv", encoding="gbk")


#找出所有VW车型对应的竞品车型
VW = ["vokswagen rabbit","volkswagen 1131 deluxe sedan","volkswagen model 111","volkswagen type 3",
    "volkswagen 411 (sw)","volkswagen super beetle","volkswagen dasher","vw dasher","vw rabbit",
    "volkswagen rabbit","volkswagen rabbit custom"]
for vw in VW:
    #提取VW车型对应的聚类结果编号
	VW_cluster_num = result[result["CarName"].isin([vw])]["聚类结果"].tolist()
    #提取与VW车型相同聚类结果的车型竞品名称
	Competitor_names = result.loc[result["聚类结果"]==int(VW_cluster_num[0])]["CarName"]
	Competitor_list=[]
	for i in Competitor_names:
		if i != vw: #去除竞品车型列表中与自身车型重复的名称
			Competitor_list.append(i)
	Competitor_name_string = ", ".join(Competitor_list) #以逗号分隔竞品车型名称列表并转化为字符串
	print(str(vw)+" 的竞争车型有："+Competitor_name_string+"\n") #打印各VW车型对应竞品车型名称














    
