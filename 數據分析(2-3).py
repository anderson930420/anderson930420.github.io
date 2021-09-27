stats1 = input('請輸入資料，並用空白鍵隔開: \n').split()
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
print(sum)
print(ave1)
print(variance1)
print(standard_deviation1)

stats2 = input('請輸入資料，並用空白鍵隔開: \n').split()
sum = 0
AA = 0
BB = 0
variance2 = 0
standard_deviation2 = 0
for i in range(len(stats2)):
     sum = sum + int(stats2[i])       #算出總和
     ave2 = sum/len(stats2)           #算出平均值
     AA = AA + (int(stats2[i]))**2    #每個資料的平方和
     BB = AA-len(stats2)*(ave2**2)    #離均差的平方和
variance2 = BB/len(stats2)
standard_deviation2 = variance2**0.5
print(sum)
print(ave2)
print(variance2)
print(standard_deviation2)