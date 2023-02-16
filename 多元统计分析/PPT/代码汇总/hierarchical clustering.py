# Project: mymom's board
# Author: Wu Jiayi Zhejiang University of Technology
# @time: 2022-01-18 20:55 

import scipy.cluster.hierarchy as hc
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import scale
import numpy as np

# 读取数据
data = pd.read_excel(r'数据\3 聚类分析\案例数据\2017年浙江省各地级市综合发展水平.xlsx', sheet_name=1)
city_name = np.array(data['地区'])
data_city = data.drop('地区', axis=1)

# 标准化
data_city = np.array(scale(data_city))

# 系统聚类
z = hc.linkage(data_city, method='ward')
print(z)

# 画聚类图
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
dd = hc.dendrogram(z, orientation='right', labels=city_name)
plt.show()
