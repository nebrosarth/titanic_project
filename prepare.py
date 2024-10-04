import pandas as pd

df = pd.read_csv('initial_data/titanic.csv')
df['Age'].fillna(df['Age'].mean(), inplace=True)
df.to_csv('prepared_data/titanic.csv', index=False)