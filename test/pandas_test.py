import pandas as pd
import numpy as np

df = pd.read_csv('data.cvs')
print(df)
print(df.dropna())
