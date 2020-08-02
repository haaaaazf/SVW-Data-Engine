# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 11:19:11 2020

@author: 12339/He Zhuangfa_PCE
"""

import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# 读入原始数据
data = pd.read_csv("订单表.csv", encoding="gbk")
# 清洗数据，获得每个客户的订单
products = data.groupby(data["客户ID"])["产品名称"].value_counts().unstack()
products[products > 1] = 1
products[np.isnan(products)] = 0
print(products)

# 挖掘频繁项集,设置最小支持度为0.05（最小提升度设为1时）
frequent_itemsets = apriori(products, min_support=0.05, use_colnames=True)
frequent_itemsets = frequent_itemsets.sort_values(by="support", ascending=False, ignore_index=True)
print("-"*20, "mlxtend频繁项集", "-"*20)
print(frequent_itemsets)

# 根据频繁项集计算关联规则,设置最小提升度为1（正相关）
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
rules = rules.sort_values(by="lift", ascending=False, ignore_index=True)
rules.to_csv("product_apriori.csv", encoding="gbk")
print("-"*20, "mlxtend关联规则", "-"*20)
print(rules)