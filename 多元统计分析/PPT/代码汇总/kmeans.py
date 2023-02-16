# Project: mymom's board
# Author: Wu Jiayi Zhejiang University of Technology
# @time: 2022-01-20 18:42 

from scipy.cluster.vq import kmeans2
import pandas as pd
import numpy as np
from sklearn.preprocessing import scale

# 读取数据
data = pd.read_excel(r'数据\3 聚类分析\案例数据\2017年全国各省市居民生活质量.xlsx', sheet_name=1)
city_name = np.array(data['地区'])
data_city = data.drop('地区', axis=1)

# 标准化
data_city = np.array(scale(data_city))

# 选择初始凝聚点
minit = [data_city[9], data_city[17], data_city[26]]

# kmeans聚类
centroid, label = kmeans2(data_city, minit, minit='matrix')
# print(centroid)
# print(label)
res = [[] for i in range(len(minit))]
for i in range(len(label)):
    res[label[i]].append(city_name[i])
for i in res:
    print(i)
