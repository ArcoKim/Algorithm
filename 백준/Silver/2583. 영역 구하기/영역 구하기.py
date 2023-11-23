import sys
sys.setrecursionlimit(10**5)

def dfs(y, x):
    paper[y][x] = 0
    result[-1] += 1
    yl = [-1, 0, 0, 1]
    xl = [0, -1, 1, 0]
    for i in range(4):
        ny = y + yl[i]
        nx = x + xl[i]
        if 0 <= ny < m and 0 <= nx < n and paper[ny][nx]:
            dfs(ny, nx)

m,n,k = map(int, input().split())
paper = [[1 for i in range(n)] for j in range(m)]

for i in range(k):
    lx,ly,rx,ry = map(int, input().split())
    for j in range(m-ly-1, m-ry-1, -1):
        for k in range(lx, rx):
            paper[j][k] = 0

result = []
for i in range(m):
    for j in range(n):
        if paper[i][j]:
            result.append(0)
            dfs(i, j)

result.sort()
print(len(result))
for val in result: print(val, end=' ')