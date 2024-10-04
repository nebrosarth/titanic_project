import pandas as pd

df = pd.read_csv('prepared_data/titanic.csv')
df['Sex_encoded'] = df['Sex'].map({'male': 1, 'female': 0})
df.to_csv('prepared_data/titanic.csv', index=False)