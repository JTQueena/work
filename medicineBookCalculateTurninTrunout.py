income = 600    # + 購買
turnin = 20 # + 受讓
turnout = 30 # - 轉讓
dispense = 45+28+14+58+28+15+56+90+84+14+45+28   # - 調劑
last = 56   #上次結餘

print("上次結餘：", last)
print("+購買：", income)
print("+**受讓**：", turnin)
print("-**轉讓**：", turnout)
print("-調劑：", dispense)
print("本次結餘應為：", last + income + turnin - turnout - dispense)
print("------------------")
print("上次結餘：", last)
print("本期總收入：", income + turnin)
print("本期總支出：", turnout + dispense)
print("本次結餘應為：", last + income + turnin - turnout - dispense)

