import os
sum = 0
for file in os.listdir('.'):
    if os.path.isfile(file):
        print(file)
        sum += os.path.getsize(file)
print(sum)

import os
sum = 0
for file in os.listdir("."):
    if os.path.isfile(file):
        sum += os.path.getsize(file)
print(sum)