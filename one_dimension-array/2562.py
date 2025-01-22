n = 9
list=[]
for i in range(n):
    x = int(input())
    list.append(x)
print(max(list))

for i in range(9):
    if list[i] == max(list):
        i = i +1
        print(i)
        break