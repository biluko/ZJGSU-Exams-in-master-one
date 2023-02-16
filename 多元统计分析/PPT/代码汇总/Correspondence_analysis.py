import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_excel(r'数据/7对应分析/案例数据/tice.xlsx', sheet_name=0)
vari_name = np.array(data.columns[1:])
sample_name = np.array(data.iloc[:, :1].T)[0]
data_vari = data.iloc[:, 1:]
print(vari_name)
print(sample_name)

data_vari = data_vari / data_vari.sum().sum()
data_sumi = np.mat(data_vari.sum())
data_sumj = np.mat(data_vari.sum(axis=1))

temp = data_sumj.T * data_sumi
data_z = np.mat((data_vari - temp) / np.sqrt(temp))

r = np.mat(data_z) * np.mat(data_z).T
Eig_Val, Eig_vec = np.linalg.eig(r)
sort_index = np.argsort(-Eig_Val)
Eig_Val = Eig_Val[sort_index][:2]
Eig_vec = Eig_vec.T[sort_index][:2].T
loadings_r = np.multiply(Eig_vec, np.sqrt(Eig_Val))
for i, j in enumerate(loadings_r):
    loadings_r[i] = np.divide(j, np.sqrt(data_sumj[0, i]))
print(loadings_r)

q = np.mat(data_z).T * np.mat(data_z)
Eig_Val, Eig_vec = np.linalg.eig(q)
sort_index = np.argsort(-Eig_Val)
Eig_Val = Eig_Val[sort_index][:2]
Eig_vec = Eig_vec.T[sort_index][:2].T
loadings_q = np.multiply(Eig_vec, np.sqrt(Eig_Val))
for i, j in enumerate(loadings_q):
    loadings_q[i] = np.divide(j, np.sqrt(data_sumi[0, i]))
print(loadings_q)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
coordinate_r = np.array(loadings_r.T)
coordinate_q = np.array(loadings_q.T)
plt.scatter(x=coordinate_r[0], y=coordinate_r[1])
plt.scatter(x=coordinate_q[0], y=coordinate_q[1])
for i, j in enumerate(sample_name):
    plt.text(coordinate_r[0][i] + 0.005, coordinate_r[1][i] + 0.005, sample_name[i])
for i, j in enumerate(vari_name):
    plt.text(coordinate_q[0][i] + 0.005, coordinate_q[1][i] + 0.005, vari_name[i])
plt.show()
