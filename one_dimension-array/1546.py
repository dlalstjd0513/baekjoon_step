N = int(input())

avr = []

score = list(map(int,input().split()))

for i in range(N):
    x = max(score)
    a = score[i]/x*100
    avr.append(a)

result = sum(avr)
aver = result/len(avr)
print(aver)