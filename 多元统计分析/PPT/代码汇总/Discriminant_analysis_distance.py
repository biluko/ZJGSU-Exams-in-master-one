import numpy as np
from scipy.spatial.distance import mahalanobis
import pandas as pd


def DDA(x_test, x_train, train_label):
    temp = x_train.join(train_label)
    train_groups = temp.groupby(temp.columns[-1])
    mu = train_groups.mean()
    mu = np.array(mu)
    train_groups = list(train_groups)
    cov = []
    label_dic = []
    for group in range(len(train_groups)):
        label_dic.append(train_groups[group][0])
        group_data = train_groups[group][1].drop('TYPE', axis=1)
        group_data = np.array(group_data)
        cov.append(np.cov(group_data.T,ddof=1))
    res = []
    for train in np.array(x_train):
        dis = []
        for j in range(len(mu)):
            d = mahalanobis(train, mu[j], np.mat(cov[j]).I)
            dis.append(float(d))
        res.append(dis.index(min(dis)))
    for test in np.array(x_test):
        dis = []
        for j in range(len(mu)):
            d = mahalanobis(test, mu[j], np.mat(cov[j]).I)
            dis.append(float(d))
        res.append(dis.index(min(dis)))

    for i in range(len(res)):
        print(i + 1, label_dic[res[i]])


train_num = 50
variables_num = 11
test_num = 48
train_data = pd.read_excel('数据/4判别分析/案例数据/enterprise_classified.xlsx')
test_data = pd.read_excel('数据/4判别分析/案例数据/enterprise_unclassified.xlsx')

DDA(test_data.iloc[:, 1:1 + variables_num], train_data.iloc[:, 1:1 + variables_num],
    train_data.iloc[:, 1 + variables_num:2 + variables_num])

# train_num = 9
# variables_num = 3
# test_num = 1
# train_data = pd.read_excel('数据/4判别分析/例题数据/Examp42.xlsx')
#
# DDA([[6,8,8]], train_data.iloc[:, :variables_num],
#     train_data.iloc[:, variables_num:1 + variables_num])

