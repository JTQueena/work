import pandas as pd
df=pd.read_csv("831.csv", encoding="utf-8")
condition=df['need'] >= 1
#print(condition)
filteredData=df[condition]
print(filteredData[['name', 'need']])
n=input()
