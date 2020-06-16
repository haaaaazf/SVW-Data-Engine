# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 09:18:39 2020
@author: SVW 12339 He Zhuangfa
"""
import pandas as pd
from pandas import DataFrame
a=DataFrame(data={"语文":[68,95,98,90,80],"数学":[65,76,86,88,90],"英语":[30,98,88,77,90]},
            index=["张飞","关羽","刘备","典韦","许褚"])
b=a.sum(axis=1)

print("三门课程的平均成绩为:","\n",a.mean(),sep='')
print("三门课程的最低成绩为:","\n",a.min(),sep='')
print("三门课程的最高成绩为:","\n",a.max(),sep='')
print("三门课程的成绩方差为:","\n",a.var(),sep='')
print("三门课程的成绩标准差为:","\n",a.std(),sep='')
print("三个人的总成绩及排名为:","\n",b.sort_values(ascending=False),sep='')