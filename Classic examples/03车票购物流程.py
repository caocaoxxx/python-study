dict_tikets={
    'G1569':['北京南-天津南','18:06','00:36'],
    'G1567':['北京南-天津南','18:15','00:34'],
    'G8917':['北京南-天津西','19:19','00:59'],
    'G203':['北京南-天津南','18:35','00:34']
}
print('车次     出发站-到达站         出发时间         到达时间')
for key in dict_tikets.keys():
    print(key,end='\t ')
    for item in dict_tikets.get(key):
        print(item,end='\t \t') 
    print()
train_no=input('请输入要购买的车次:')
info=dict_tikets.get(train_no,'车次不存在')
s = info[0]+' '+info[1]+'开'
if info!='车次不存在':
    passenger=input('请输入乘车人:')
    print(f'您已购买{train_no},{s},请{passenger}尽快乘车')
else:
    print('您输入的车次可能不存在')
