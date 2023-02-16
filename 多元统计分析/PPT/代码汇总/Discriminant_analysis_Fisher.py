from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import numpy as np
import pandas as pd

train_data = pd.read_excel('数据/4判别分析/案例数据/flower.xlsx')
train_label = np.array(train_data['类型A'])
x_tain = np.array(train_data.drop('类型A', axis=1))

lda = LinearDiscriminantAnalysis()
lda.fit(x_tain, train_label)
res = lda.predict(x_tain)
cnt = 0
for i in range(len(res)):
    if res[i] != train_label[i]:
        flag = 0
        cnt += 1
    else:
        flag = 1
    print(i + 1, x_tain[i], res[i], train_label[i], flag)

print('train currency= %f' % (1 - cnt / len(res)))
