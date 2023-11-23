import sys
input = sys.stdin.readline

def dfs(y, x):
    arr[y][x] = 0
    yl = [0, -1, 1, 0]
    xl = [-1, 0, 0, 1]
    for i in range(4):
        if 0 <= y + yl[i] < n and 0 <= x + xl[i] < m and arr[y + yl[i]][x + xl[i]]:
            dfs(y + yl[i], x + xl[i])

t = int(input())
for _ in range(t):
    m,n,k = map(int, input().split())
    arr = [[0 for i in range(m)] for j in range(n)]
    for i in range(k):
        x,y = map(int, input().split())
        arr[y][x] = 1

    result = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                result += 1
                dfs(i, j)
    print(result)