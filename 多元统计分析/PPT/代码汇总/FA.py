import numpy as np
import pandas as pd
from factor_analyzer import FactorAnalyzer

# 读取数据
data = pd.read_excel(r'数据/6 因子分析/例题数据/studyf.xlsx', sheet_name=0)
vari_name = np.array(data.columns[1:])
data_vari = data.iloc[:, 1:]
data_vari = (data_vari - np.average(data_vari, axis=0)) / np.std(data_vari, axis=0, ddof=1)

fa = FactorAnalyzer(3, method='principal', rotation="varimax")
fa.fit(data_vari)
print(fa.loadings_)
# print(fa.get_communalities())
# print(fa.get_eigenvalues())
