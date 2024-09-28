lst=[1,2,3,4,5]
def sum_of_lst(list):
    sum=0
    for num in lst:
        sum+=num
    return sum
print(f'{lst}的和为',sum_of_lst(lst))