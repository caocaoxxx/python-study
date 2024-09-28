L1=[88,89,90,98,00,99]
# L2['1988','1989','1990','2000','1999'] #修改后的列表
# #遍历列表的方式
# for index in range(len(L1)):
#     if L1[index]==0:
#         L1[index]='200'+str(L1[index])
#     else:
#         L1[index]='19'+str(L1[index])
# print(L1)

#使用enumerate函数
for index,value in enumerate(L1):
    if L1[index]==0:
        L1[index]='200'+str(value)
    else:
        L1[index]='19'+str(value)
print(L1)
