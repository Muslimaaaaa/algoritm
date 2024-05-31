import random
import time
from datetime import datetime

data = list(set([1, 1, 6, 13, 14, 14, 23, 23, 26, 26, 30, 31, 32, 32, 37, 42, 44, 47, 48, 50]))
data_l = len(data) - 1
data.sort()
print(data)

target = int(input("Target: "))
low = 0
data_l = len(data) - 1
count = 0
while True:
    count += 1
    middle = (data_l + low) // 2
    if data[middle] < target:  # false
        low = middle + 1
    elif data[middle] == target:
        print(target)
        print(f"Count {count}")
        break
    else:
        data_l = middle






