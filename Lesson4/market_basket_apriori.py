# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 14:13:31 2020
@author: He Zhuangfa/PCE
"""

import pandas as pd
import numpy as np

from efficient_apriori import apriori

#导入数据，由于数据是rawdata，不将第一行作为Head
data = pd.read_csv("Market_Basket_Optimisation.csv",header = None)
print(data.shape)

# efficient_apriori参数需要列表或元祖,将data透视表的数据放到transactions列表
transactions = []
for i in range(0,data.shape[0]):
    temp = []
    for j in range(0,data.shape[1]):
        # print(data.values[i,j])，得知内部空值为"nan"
        if str(data.values[i, j]) !='nan':
            temp.append(str(data.values[i,j])) #将列表值添加到temp中
    transactions.append(temp)

#方法一：简单挖掘apriori算法
#挖掘频繁项集与关联规则，通过不断修改Min值确定最优频繁项集和关联规则
itemsets, rules = apriori(transactions, min_support=0.05, min_confidence=0.15)
print('efficient频繁项集：\n', itemsets)
print('efficient关联规则：\n', rules)

#-----------------------------------------------------------------------------------------
#方法二：mlxtend挖掘apriori算法
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder

# mlxtend apriori需要进行独热编码后的参数，先对数据进行独热编码
temp2 = TransactionEncoder()
temp2_hot_encoded = temp2.fit(transactions).transform(transactions)
#print(temp2_hot_encoded)
df = pd.DataFrame(temp2_hot_encoded, columns=temp2.columns_)
print(df)

# 挖掘频繁项集,设置最小支持度为0.05（最小提升度设为1时）
frequent_itemsets = apriori(df, min_support=0.05, use_colnames=True)
frequent_itemsets = frequent_itemsets.sort_values(by='support', ascending=False, ignore_index=True)
print('-'*20, 'mlxtend频繁项集', '-'*20)
print(frequent_itemsets)

# 根据频繁项集计算关联规则,设置最小提升度为1（正相关）
rules = association_rules(frequent_itemsets, metric='lift', min_threshold=1)
rules = rules.sort_values(by='lift', ascending=False, ignore_index=True)
rules.to_csv('market_basket_apriori.csv')
print('-'*20, 'mlxtend关联规则', '-'*20)
print(rules)