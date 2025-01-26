N, M = map(int,input().split())

basket = [0]*N #바구니 갯수

for i in range(N):
    basket[i] = i+1


for i in range(M):
    i, j = map(int,input().split())
    basket[i-1:j] = basket[i-1:j][::-1]

for x in range(N):
  print(basket[x], end=" ")