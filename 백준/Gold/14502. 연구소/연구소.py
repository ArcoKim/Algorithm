import sys
import copy
from itertools import combinations
input = sys.stdin.readline

def dfs(y, x):
    new_area[y][x] = 2
    yl = [-1, 0, 0, 1]
    xl = [0, -1, 1, 0]
    for i in range(4):
        ny = y + yl[i]
        nx = x + xl[i]
        if 0 <= ny < n and 0 <= nx < m and not new_area[ny][nx]:
            dfs(ny, nx)

n,m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

zeros = []
virus = []
for i in range(n):
    for j in range(m):
        if area[i][j] == 0:
            zeros.append((i,j))
        if area[i][j] == 2:
            virus.append((i,j))

result = 0
for pair in combinations(zeros, 3):
    new_area = copy.deepcopy(area)
    new_area[pair[0][0]][pair[0][1]] = 1
    new_area[pair[1][0]][pair[1][1]] = 1
    new_area[pair[2][0]][pair[2][1]] = 1
    for loc in virus:
        dfs(loc[0], loc[1])
    result = max(result, sum(x.count(0) for x in new_area))

print(result)