import pandas as pd
df=pd.read_csv("JTistheQueen.csv")
while True:
    key=input("請輸入完整健保碼：")
    condition=df['藥品代號']==key
    #print(condition)
    filteredData=df[condition]
    print(filteredData[['藥品英文名稱', '藥品中文名稱','成份']])
    key2=input("藥品名稱：")
    key3=input("數量：")
    openfile = open("DO_NOT_OPEN.txt", mode="a")
    print(key, key2, key3, file=openfile)
    openfile.close()
    print()
