import pandas as pd
df=pd.read_csv("JTistheQueen.csv")
while True:
    key=input("請輸入健保碼(可模糊搜尋)：")
    condition=df['藥品代號'].str.contains(key)
    #print(condition)
    filteredData=df[condition]
    print(filteredData[['藥品英文名稱', '藥品中文名稱','成份']])
    #print(filteredData[['藥品代號']])
    print("----------------")
'''
while True:
    key=input("請輸入完整健保碼：")
    v1=df[df.loc[:,'藥品代號']==key]
    print(v1[['藥品英文名稱', '藥品中文名稱','成份']])
    print("----------------")
'''
