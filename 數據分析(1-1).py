#輸入10筆資料
A = input("請輸入A1： ")
B = input("請輸入B1： ")
C = input("請輸入C1： ")
D = input("請輸入D1： ")
E = input("請輸入E1： ")
F = input("請輸入F1： ")
G = input("請輸入G1： ")
H = input("請輸入H1： ")
I = input("請輸入I1： ")
J = input("請輸入J1： ")
#將10筆資料存入stats陣列
stats = [int(A),int(B),int(C),int(D),int(E),int(F),int(G),int(H),int(I),int(J)]
#算出總合與平均值
sum = 0
for i in range(10):
     sum = sum + stats[i]
     ave = sum/10
print(sum)
print(ave)


