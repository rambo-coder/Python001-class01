import pandas as pd
import numpy as np

x = pd.Series([1,2,np.nan,3,4,5,6,np.nan,8])

# print(x.hasnans)
x=x.fillna(value=x.mean())
# print(x)

# 前向填充缺失值

df3=pd.DataFrame({"A":[5,3,None,4],
                 "B":[None,2,4,3],
                 "C":[4,3,8,5],
                 "D":[5,4,2,None]})
print(df3)
print('*'*20)
print(df3.isnull().sum())

# df3 = df3.ffill(axis=1)
print('*'*20)
print(df3)

# print(df3.info)
# df3=df3.dropna()
# print(df3)

print(df3.drop_duplicates())