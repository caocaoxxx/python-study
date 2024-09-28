import datetime
current_time = datetime.datetime.now()
print(current_time)
#格式化打印字符串
str_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(str_time)
#
print("year:",current_time.year)
print("month:",current_time.month)
print("day:",current_time.day)
print("hour:",current_time.hour)
print("minute:",current_time.minute)
print("second:",current_time.second)
print("weekday:",current_time.weekday())
print("isoweekday:",current_time.isoweekday())
