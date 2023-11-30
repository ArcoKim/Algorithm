import sys, copy
input = sys.stdin.readline

maps = []
n,m = map(int, input().split())
zeros = []
for i in range(n):
    now = list(map(int, input().split()))
    maps.append(now)
    for j in range(m):
        if now[j] == 0:
            zeros.append([i, j])

def dfs(i, j):
    comb1 = [0, -1, 1, 0]
    comb2 = [-1, 0, 0, 1]
    for k in range(4):
        ni = i + comb1[k]
        nj = j + comb2[k]
        if 0 <= ni < n and 0 <= nj < m and cpmaps[ni][nj] == 0:
            cpmaps[ni][nj] = 2
            dfs(ni, nj)

result = 0
for i in range(len(zeros)):
    for j in range(i+1, len(zeros)):
        for k in range(j+1, len(zeros)):
            cpmaps = copy.deepcopy(maps)
            cpmaps[zeros[i][0]][zeros[i][1]] = 1
            cpmaps[zeros[j][0]][zeros[j][1]] = 1
            cpmaps[zeros[k][0]][zeros[k][1]] = 1
            for l in range(n):
                for o in range(m):
                    if cpmaps[l][o] == 2:
                        dfs(l, o)
            tmpR = 0
            for l in range(n):
                for o in range(m):
                    if cpmaps[l][o] == 0:
                        tmpR += 1
            result = max(result, tmpR)
print(result)
