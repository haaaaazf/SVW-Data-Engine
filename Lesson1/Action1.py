# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 09:18:39 2020
@author: SVW 12339 He Zhuangfa
"""
#方法1---------------------------------------
import numpy as np
a=np.arange(2,101,2)
b=np.sum(a)
print("求和结果为：{}".format(b))

#方法2---------------------------------------
a=sum(range(2,101,2))
print("求和结果为：{}".format(a))

#方法3--------------------------------------
a=0
for i in range(2,101,2):
    a+=i
print("求和结果为：{}".format(a))