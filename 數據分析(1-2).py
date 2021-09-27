stats1 = list()
stats1.append(input("請輸入10筆資料\n"))   #輸入10筆資料
while True:
    b = input()
    if len(stats1) in range(10):
        stats1.append(b)
    else:
        break
print(stats1)

sum = 0
for i in range(10):
     sum = sum + int(stats1[i])          #算出總合
     ave = sum/10                        #算出平均
print(sum)
print(ave)