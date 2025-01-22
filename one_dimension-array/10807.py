import random
n = int(input())
sum = 0
list = []

for i in range(n):
    x =random.randint(-100,100)
    list.append(x)

for i in range(n):
    print(list[i],' ', end='')
print()

v = int(input())

for i in range(n):
    if list[i] == v:
        sum = sum +1

print(sum)