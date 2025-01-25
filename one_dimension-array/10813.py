N, M = map(int,input().split())
basket = [0]*N

#바구니 속 공의 번호 저장
for i in range (N):
    basket[i] = i+1

for y in range(M):
    i, j = map(int,input().split())
    h = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = h

for i in range(N):
    print(basket[i], end=' ')