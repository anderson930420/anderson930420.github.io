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
for i in range(10):
     sum = sum + int(stats1[i])
     ave = sum/10
print(sum)
print(ave)


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
for i in range(10):
     sum = sum + int(stats2[i])
     ave = sum/10
print(sum)
print(ave)
