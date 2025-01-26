list = []
arr = []

for i in range(10):
    n=int(input())
    list.append(n)

for i in range(10):
    n = list[i]%42
    list[i] = n

for i in range(10):
    if list[i]%42 not in arr:
        arr.append(list[i] % 42)

print(len(arr))