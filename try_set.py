import datetime
import random
a = [random.randint(0, 100000000)for i in range(1000000)]
checked_list = [random.randint(0, 100000000)for i in range(100)]

x = datetime.datetime.now()

for temp in checked_list:
    if temp in a:
        print(f'temp:{temp} in a')

y = datetime.datetime.now()
print(y-x)

b = set(a)
for temp in checked_list:
    if temp in b:
        print(f'temp:{temp} in a')

z = datetime.datetime.now()
print(z-y)