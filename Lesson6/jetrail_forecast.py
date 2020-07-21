# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 10:48:40 2020

@author: 86180
"""

import pandas as pd
from fbprophet import Prophet

#数据加载
train = pd.read_csv("train.csv",encoding = "gbk")
print(train.head())

#转换为pandas中的日期格式
train["Datetime"] = pd.to_datetime(train.Datetime, format="%d-%m-%Y %H:%M")
#将Datetime作为train的索引
train.index = train.Datetime
print(train.head())
#去掉ID列和重复的Datetime列
train = train.drop(["ID","Datetime"], axis=1)
print(train.head())

#按照天进行采样
daily_train = train.resample("D").sum()
print(daily_train.head())
daily_train["ds"] = daily_train.index
daily_train["y"] = daily_train.Count #设置为ds、y的保留字
print(daily_train.head())
daily_train.drop(["Count"], axis=1, inplace=True)
print(daily_train.head())

#拟合Prophet模型并做训练
model = Prophet(yearly_seasonality=True, daily_seasonality=True, seasonality_prior_scale=0.1)
model.fit(daily_train)
#预测未来7个月，213天
future = model.make_future_dataframe(periods=213)
forecast = model.predict(future)
print(forecast)
model.plot(forecast)
#查看各个成分
model.plot_components(forecast)

# 对节假日建模
# 将节日看成是一个正态分布，把活动期间当做波峰，lower_window 以及upper_window 的窗口作为扩散
chinese_seasons = pd.DataFrame({
  'holiday': 'chinese_season',
  'ds': pd.to_datetime(['2012-01-01', '2012-05-01', '2012-10-01',
                        '2013-01-01', '2013-05-01', '2013-10-01',
                        '2014-01-01', '2014-05-01', '2014-10-01',
                        '2015-01-01', '2015-05-01', '2015-10-01']),
  'lower_window': 0,
  'upper_window': 1,
})
print(chinese_seasons)

model = Prophet(holidays=chinese_seasons, daily_seasonality=True)
model.fit(daily_train)
future = model.make_future_dataframe(periods=213)
forecast = model.predict(future)
#print(forecast.tail())
# 预测的成分分析绘图，展示预测中的趋势、周效应和年度效应,holidays项
model.plot_components(forecast)
#print(forecast.columns)