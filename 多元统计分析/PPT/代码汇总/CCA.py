import numpy as np
from sklearn.preprocessing import scale
import pandas as pd

num_X = 4
num_Y = 5
num = min(num_X, num_Y)

data = pd.read_excel('数据/8典型相关分析/案例数据/tech.xlsx')
X = np.array(data[['x1', 'x2', 'x3', 'x4']])
Y = np.array(data[['y1', 'y2', 'y3', 'y4', 'y5']])
X = scale(X)
Y = scale(Y)

R = np.corrcoef(X.T, Y.T)
R11 = np.mat(R[:num_X, :num_X])
R22 = np.mat(R[num_X:num_X + num_Y, num_X:num_X + num_Y])
R12 = np.mat(R[:num_X, num_X:num_X + num_Y])
R21 = np.mat(R[num_X:num_X + num_Y, :num_X])
R11_inv = np.linalg.inv(R11)
R22_inv = np.linalg.inv(R22)

M1 = R11_inv * R12 * R22_inv * R21
M2 = R22_inv * R21 * R11_inv * R12

e1, v1 = np.linalg.eig(M1)
print('特征值：')
print(e1)
print('相关系数：')
print(np.sqrt(e1))
print('M1特征向量：')
print(v1)

e2, v2 = np.linalg.eig(M2)
print('M2特征向量：')
print(v2)

v1 = v1[:, :num]
v2 = v2[:, :num]

V = np.mat(X) * np.mat(v1)
W = np.mat(Y) * np.mat(v2)
corr1 = np.corrcoef(X.T, V.T)[:num_X,num_X:]
corr2 = np.corrcoef(Y.T, W.T)[:num_Y,num_Y:]
print('典型结构1')
print(corr1)
print('典型结构2')
print(corr2)

