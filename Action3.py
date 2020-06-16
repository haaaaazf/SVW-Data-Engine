# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 09:18:39 2020
@author: SVW 12339 He Zhuangfa
"""
import pandas as pd

#数据加载-------------------------------------
a=pd.read_csv("C:/Users/86180/Desktop/Python练习/SVW Data Engine/Data_Engine_with_Python-master/L1/car_data_analyze/car_complain.csv")
print(a)

#数据预处理-----------------------------------
a=a.drop("problem",1).join(a.problem.str.get_dummies(","))
print(a)
a.to_csv("C:/Users/86180/Desktop/Python练习/SVW Data Engine/Output1.csv")

#数据统计-------------------------------------
b = a.groupby(["brand"])["id"].agg(["count"]).sort_values("count", ascending=False)
print("品牌投诉总数\n", b,)
b.to_csv("C:/Users/86180/Desktop/Python练习/SVW Data Engine/Output2.csv")

c= a.groupby(["car_model"])["id"].agg(["count"]).sort_values("count", ascending=False)
print("车型投诉总数\n", c)
c.to_csv("C:/Users/86180/Desktop/Python练习/SVW Data Engine/Output3.csv")

d = a.groupby(["brand", "car_model"])["id"].agg(["count"]).groupby(["brand"]).mean().\
    sort_values("count", ascending=False)
print("平均品牌车型投诉总数\n",d)
d.to_csv("C:/Users/86180/Desktop/Python练习/SVW Data Engine/Output4.csv")
