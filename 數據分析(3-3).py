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

sum = 0
AA = 0
BB = 0
variance1 = 0
standard_deviation1 = 0
for i in range(len(stats1)):
     sum = sum + int(stats1[i])       #算出總和
     ave1 = sum/len(stats1)           #算出平均值
     AA = AA + (int(stats1[i]))**2    #每個資料的平方和
     BB = AA-len(stats1)*(ave1**2)  #離均差的平方和
variance1 = BB/len(stats1)
standard_deviation1 = variance1**0.5
print("英文成績",nums1)
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

sum2 = 0
AA = 0
BB = 0
variance2 = 0
standard_deviation2 = 0
for i in range(len(stats2)):
     sum2 = sum2 + int(stats2[i])       #算出總和
     ave2 = sum2/len(stats2)           #算出平均值
     AA = AA + (int(stats2[i]))**2    #每個資料的平方和
     BB = AA-len(stats2)*(ave2**2)  #離均差的平方和
variance2 = BB/len(stats2)
standard_deviation2 = variance2**0.5
print("數學成績",nums2)
print("總和 =",sum2)
print("平均 =",ave2)
print("變異數 =",variance2)
print("標準差 =",standard_deviation2)

b = (variance1**0.5)*(variance2**0.5)/variance1
a = ave2-b*ave1
print("\n設回歸線方程式為y=a+bx\n則 b =",b,"將兩資料平均數分別帶入可得a =" ,a,"\n可得回歸線方程式: y=",a,"+",b,"x")
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

x = np.linspace(1,100, 100)
y = a+b*x

相關係數 = (SUM-len(stats1)*ave1*ave2)/(len(A)*standard_deviation1*standard_deviation2)

plt.plot(listx1,listy1,'r.', label='Data point')
plt.plot(x,y, label='Linear Regression ')
plt.legend(loc='best')
plt.show()
''' print(listx1)
    print(listy1)
    print(A)
    print(SUM) '''
print("相關係數=",相關係數)
number_condition_p = "正"
number_condition_m = "負"
positive_number_condition = True
while positive_number_condition == True:
    if 相關係數*(-1)>0:
        positive_number_condition = False
    elif 相關係數*(-1)<0:
        positive_number_condition = True
r_abs = abs(相關係數)
while 1:
    if r_abs == 0:
        print("為 零相關")
    elif 0<r_abs<0.3:
        if positive_number_condition == True :
            print("為 低度",number_condition_p,"相關")
            break
        else :
            print("為 低度",number_condition_m,"相關")
            break
    elif 0.3<=r_abs<0.7:
        if positive_number_condition == True:
            print("為 中度",number_condition_p,"相關")
            break
        else:
            print("為 中度",number_condition_m,"相關")
            break
    elif 0.7<=r_abs<1:
        if positive_number_condition == True:
            print("為 高度",number_condition_p,"相關")
            break
        else:
            print("為 高度",number_condition_m,"相關")
            break
print("-------------------------------------------------------------")
print("\n分析結束")
#plt.savefig('stats_figure.png')