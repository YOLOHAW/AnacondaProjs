import pandas as pd
df=pd.read_csv('pokemon.csv')
df.head()

df['Type 2'].value_counts().plot()
