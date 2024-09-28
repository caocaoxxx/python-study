lis1=[1,2,3,44,44,33,33]
lst=[]
for item in lis1:
    if item not in lst:
        lst.append(item)
print(lst)