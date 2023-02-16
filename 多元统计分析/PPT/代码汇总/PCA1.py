# Project: mymom's board
# Author: Wu Jiayi Zhejiang University of Technology
# @time: 2022-03-03 19:16 

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA as skPCA

# 读取数据
data = pd.read_excel(r"数据\5主成分分析\案例数据\economic.xlsx")
vari_name = np.array(data.columns[1:])
city_name = np.array(data['region'])
data_vari = data.iloc[:, 1:]
data_vari = (data_vari - np.average(data_vari, axis=0)) / np.std(data_vari, axis=0, ddof=1)

pca = skPCA(n_components=len(vari_name))
pca.fit(data_vari)

EigenValue_table = pd.DataFrame(pca.explained_variance_, columns=['Eigenvalue'], index=list(range(1, 11)))
prop = EigenValue_table['Eigenvalue'] / EigenValue_table['Eigenvalue'].sum()
cumulative = []
sum = 0
for i in prop:
    sum += i
    cumulative.append(sum)
EigenValue_table['Proportion'] = prop
EigenValue_table['Cumulative'] = cumulative
print(EigenValue_table)

EigenVector_table = pd.DataFrame(pca.components_[:3, :], index=['Prin1', 'Prin2', 'Prin3'], columns=vari_name).T
print(EigenVector_table)

Score_table = pd.DataFrame(pca.transform(data_vari)[:, 0:2], index=city_name, columns=['Prin1_Score', 'Prin2_Score'])
Score_table = Score_table.sort_values('Prin1_Score', ascending=False)
print(Score_table)
