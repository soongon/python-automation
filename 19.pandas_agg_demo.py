import pandas as pd

df = pd.read_csv('./data/salaries_backup.csv')
# print(df)

# 2000년 이후 NL 의 모든 선수의 평균 연봉
df = df.loc[(df['yearID'] >= 2000) & (df['lgID'] == 'NL')]
# print(df)

print(df['salary'].mean())
