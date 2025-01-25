list = [0]*30

for i in range(30):
    list[i] = i+1

for i in range(28):
    n = int(input())
    list.remove(n)
            
print(min(list))
print(max(list))