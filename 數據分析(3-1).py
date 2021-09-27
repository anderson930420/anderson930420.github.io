import numpy as np
import matplotlib.pyplot as plt
#輸入第一筆資料
stats1 = input('請輸入資料，並用空白鍵隔開: \n').split()
condition = True
nums1 = []   #儲存得到的資料
while condition == True :
 for n in stats1:
      if n.isdigit():      #檢查是不是整數
         nums1 += [int(n)]
         condition = False
      else:
          print("無效的資料，請重新輸入")
          stats1 = input('請輸入資料，並用空白鍵隔開: \n').split()
          condition = True
          break
print("英文成績 = ",nums1)

sum = 0
AA = 0
BB = 0
variance1 = 0
standard_deviation1 = 0
for i in range(len(stats1)):
     sum = sum + int(stats1[i])       #算出總和
     ave1 = sum/len(stats1)           #算出平均值
     AA = AA + (int(stats1[i]))**2    #每個資料的平方和
     BB = AA-len(stats1)*(ave1**2)    #離均差的平方和
variance1 = BB/len(stats1)
standard_deviation1 = variance1**0.5
print("總和 =",sum)
print("平均 =",ave1)
print("變異數 =",variance1)
print("標準差 =",standard_deviation1,"\n")

#輸入第二筆資料
stats2 = input('請輸入資料，並用空白鍵隔開: \n').split()
condition = True
nums2 = []   #儲存得到的三個數
while condition == True :
 for n in stats2:
      if n.isdigit():      #檢查是不是整數
         nums2 += [int(n)]
         condition = False
      else:
          print("無效的資料，請重新輸入")
          stats2 = input('請輸入資料，並用空白鍵隔開: \n').split()
          condition = True
          break
print("數學成績 = ",nums2)
sum2 = 0
AA = 0
BB = 0
variance2 = 0
standard_deviation2 = 0
for i in range(len(stats2)):
     sum2 = sum2 + int(stats2[i])       #算出總和
     ave2 = sum2/len(stats2)            #算出平均值
     AA = AA + (int(stats2[i]))**2      #每個資料的平方和
     BB = AA-len(stats2)*(ave2**2)      #離均差的平方和
variance2 = BB/len(stats2)
standard_deviation2 = variance2**0.5
print("總和 =",sum2)
print("平均 =",ave2)
print("變異數 =",variance2)
print("標準差 =",standard_deviation2)

listx1 = []
listy1 = []
A = []
SUM = 0
for i in stats1 :
    listx1 += [int(i)]

for j in stats2:
    listy1 += [int(j)]

for i, j in zip(stats1, stats2):
    A = A + [np.multiply(int(i), int(j))]

for i in  A:
    SUM += int(i)

plt.title("Does English grades effect Math grades ?",fontsize=16)
plt.xlabel("English",fontsize=14)
plt.ylabel("Math",fontsize=14)
plt.xlim(0,100)
plt.ylim(0,100)

plt.plot(listx1,listy1,'r.', label='Data point')
plt.show()
