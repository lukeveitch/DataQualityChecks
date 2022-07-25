import pandas as pd
df = pd.read_csv('MOCK_DATA.csv')
print(df.columns)

print(df.info())
print(df.describe())
print(df.describe(include=object))
print('\n\n\nNumber of nulls:\n')
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.drop_duplicates())