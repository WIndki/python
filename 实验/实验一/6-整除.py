# 求1~100之间能被7整除，但不能同时被5整除的所有整数
result = [i for i in range(1, 101) if i % 7 == 0 and i % 5 != 0]
print(result)