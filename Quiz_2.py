Exchange = {'달러' : 1320, '엔' : 950, '위안' : 182}
money = [13, 200, 13]
dollar = Exchange['달러'] * money[0]
Yen = Exchange['엔'] * money[1]
Yuan = Exchange['위안'] * money[2]
total = dollar + Yen + Yuan
a = "철수가 가지고 있는 돈의 원화 가치는 %d원 입니다." %(total)
print(a)
