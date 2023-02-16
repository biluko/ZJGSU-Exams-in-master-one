# Project: mymom's board
# Author: Wu Jiayi Zhejiang University of Technology
# @time: 2022-03-03 19:16 

import numpy as np
import pandas as pd


def PCA(x, components=None):
    if components == None:
        components = int(x.size / len(x))
    average = np.mean(x, axis=0)
    sigma = np.std(x, axis=0, ddof=1)
    r, c = np.shape(x)
    mu = np.tile(average, (r, 1))
    data_std = (x - mu) / sigma
    cov_matrix = np.cov(data_std.T)
    EigenValue, EigenVector = np.linalg.eig(cov_matrix)
    index = np.argsort(-EigenValue)
    Selected_Vector = EigenVector.T[index[:components]] * (-1)
    Score = data_std * np.mat(Selected_Vector.T)
    return EigenValue[index], Selected_Vector, np.array(Score)

# 读取数据
data = pd.read_excel(r"数据\5主成分分析\案例数据\economic.xlsx")
vari_name = np.array(data.columns[1:])
city_name = np.array(data['region'])
data_vari = np.array(data.drop('region', axis=1))


EigenValue, Vector, Score = PCA(np.asarray(data_vari), 3)
EigenValue_table = pd.DataFrame(EigenValue, columns=['Eigenvalue'], index=list(range(1, 11)))
prop = EigenValue_table['Eigenvalue'] / EigenValue_table['Eigenvalue'].sum()
cumulative = []
sum = 0
for i in prop:
    sum += i
    cumulative.append(sum)
EigenValue_table['Proportion'] = prop
EigenValue_table['Cumulative'] = cumulative
print(EigenValue_table)

EigenVector_table = pd.DataFrame(Vector, index=['Prin1', 'Prin2', 'Prin3'], columns=vari_name).T
print(EigenVector_table)

Score_table = pd.DataFrame(Score[:, 0:2], index=city_name, columns=['Prin1_Score', 'Prin2_Score'])
Score_table = Score_table.sort_values('Prin1_Score', ascending=False)
print(Score_table)
