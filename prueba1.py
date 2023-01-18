import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings

df_train = pd.read_csv("1.csv")
a = df_train.head(20)
print(a)
b = df_train["kills"].describe()
print(b)
d = sns.displot(df_train["kills"])
print(d)
c = df_train[["kills", "team_name"]]
print(c)
#print("hola")