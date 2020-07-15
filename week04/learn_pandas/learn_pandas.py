import pandas as pd
import numpy as np
import matplotlib as plt
import os

pwd = os.path.dirname(os.path.realpath(__file__))
book = os.path.join(pwd,'book_utf8.csv')

df = pd.read_csv(book)

df.columns = ['star','vote','shorts']
print(df)
print(df.loc[1:3,['star']])
print(df.iloc[:,[1,2]])
