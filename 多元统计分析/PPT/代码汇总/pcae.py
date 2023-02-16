# Project: mymom's board
# Author: Wu Jiayi Zhejiang University of Technology
# @time: 2022-03-03 19:16 

import xlrd
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
    Selected_Vector = EigenVector.T[index[:components]]*(-1)
    Score = data_std * np.mat(Selected_Vector.T)
    return EigenValue[index], Selected_Vector, np.array(Score)


file = xlrd.open_workbook(r"数据\5主成分分析\习题数据\EXE5_1.xlsx")
table = file.sheets()[0]

# 读取数据
industry_name = []
vari_name = []
data_vari = []
for i in range(1, table.nrows):
    industry_name.append(table.cell(i, 0).value)
for i in range(1, table.ncols):
    vari_name.append(table.cell(0, i).value)
for i in range(1, table.nrows):
    data_temp = []
    for j in range(1, table.ncols):
        data_temp.append(table.cell(i, j).value)
    data_vari.append(data_temp)

EigenValue, Vector, Score = PCA(np.asarray(data_vari), 2)
EigenValue_table = pd.DataFrame(EigenValue, columns=['Eigenvalue'], index=list(range(1, 9)))
prop = EigenValue_table['Eigenvalue'] / EigenValue_table['Eigenvalue'].sum()
cumulative = []
sum = 0
for i in prop:
    sum += i
    cumulative.append(sum)
EigenValue_table['Proportion'] = prop
EigenValue_table['Cumulative'] = cumulative
print(EigenValue_table)

EigenVector_table = pd.DataFrame(Vector, index=['Prin1', 'Prin2'], columns=vari_name).T
print(EigenVector_table)

Score_table = pd.DataFrame(Score[:, 0:2], index=industry_name, columns=['Prin1_Score', 'Prin2_Score'])
Score_table = Score_table.sort_values('Prin2_Score', ascending=False)
print(Score_table)
