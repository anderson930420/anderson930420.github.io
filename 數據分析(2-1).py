#輸入第1組資料
stats1 = list()
stats1.append(input("請輸入10筆資料\n"))
while True:
    b = input()
    if len(stats1) in range(10):
        stats1.append(b)                #將輸入的資料加入陣列stats1中
    else:
        break
print(stats1)

sum = 0
for i in range(10):
     sum = sum + int(stats1[i])         #算出總和
     ave = sum/10                       #算出平均
print(sum)
print(ave)

#輸入第2組資料
stats2 = list()
stats2.append(input("\n請輸入10筆資料\n"))
while True:
    b = input()
    if len(stats2) in range(10):        
        stats2.append(b)                #將輸入的資料加入陣列stats2中                         
    else:
        break
print(stats2)

sum = 0
for i in range(10):
     sum = sum + int(stats2[i])         #算出總和                        
     ave = sum/10                       #算出平均
print(sum)
print(ave)
