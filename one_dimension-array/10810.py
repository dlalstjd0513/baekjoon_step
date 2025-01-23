"""N, M = map(int,input().split())

basket = [0] * N

for x in range(M):
    i, j, k = map(int, input().split())
    for y in range(i, i+1):
        basket[x] = k

for z in range(1, N+1):
    print(basket, end=' ')


N, M = map(int, input().split())

basket = [0] * (N)

for x in range(M):
    i, j, k = map(int, input().split())
    for y in range(i, j+1):
        basket[x-1] = k

for z in range(n):
    print(basket[x], end=' ')"""

#이 부분이 정답
n,m = map(int, input().split())

basket = [0]*n

for l in range(m):
  i,j,k = map(int,input().split())
  for x in range(i,j+1):
    basket[x-1] = k

for x in range(n):
  print(basket[x], end=" ")