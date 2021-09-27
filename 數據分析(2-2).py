#輸入10筆資料
stats1 = list()
stats1.append(input("請輸入10筆資料\n"))
while True:
    b = input()
    if len(stats1) in range(10):
        stats1.append(b)
    else:
        break
print(stats1)

sum = 0
AA = 0
BB = 0
CC = 0
zz = 0

for i in range(10):
     sum = sum + int(stats1[i])       #算出總合
     ave1 = sum/10                    #算出平均
     AA = AA + (int(stats1[i]))**2    #算出各資料平方的總和
BB = AA-10*(ave1**2)
CC = BB/10
zz = CC**0.5                          #算出標準差
print(sum)
print(ave1)
print(CC)
print(zz)

#輸入10筆資料
stats2 = list()
stats2.append(input("\n請輸入10筆資料\n"))
while True:
    b = input()
    if len(stats2) in range(10):
        stats2.append(b)
    else:
        break
print(stats2)

sum = 0
AAA = 0
BBB = 0
CCC = 0
zzz = 0
for i in range(10):
     sum = sum + int(stats2[i])         #算出總合
     ave2 = sum/10                      #算出平均
     AAA = AAA + (int(stats2[i]))**2    #算出各資料平方的總和
BBB = AAA-10*(ave2**2)
CCC = BBB/10
zzz = CCC**0.5                          #算出標準差
print(sum)
print(ave2)
print(CCC)
print(zzz)


