# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 17:07:06 2020
@author: He Zhaungfa/PCE
"""
#使用KMeans进行聚类
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd

#数据加载
data=pd.read_csv("car_data.csv",encoding="gbk")
train_x=data[["人均GDP","城镇人口比重","交通工具消费价格指数","百户拥有汽车量"]]
#print(train_x)

#将数据规范到[0,1]区间
min_max_scaler=preprocessing.MinMaxScaler()
train_x=min_max_scaler.fit_transform(train_x) #训练
print(train_x)

#使用KMeans聚类
kmeans=KMeans(n_clusters=4)
kmeans.fit(train_x) #机器训练
predict_y=kmeans.predict(train_x) #机器预测
#（问题1，想问下为啥会有训练和预测的步骤呀？）

#合并聚类结果，插入到原数据中
result=pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u"聚类结果"},axis=1,inplace=True) 
#问题2，这里的inplace=True的含义是啥啊？
print(result)
result.to_csv("car_consumption.csv",encoding="gbk")

#问题3，我想把[0,1]这四列结果也加到表格里面去，代码怎么写哇？