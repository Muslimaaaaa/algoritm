import random

data = []
for i in range (20):
    data.append(random.randint(1,50))
print(data)
target = int(input("Enter"))
if target in data:
    print(f""" {target} Target""")
else:
    print("Not Target")

