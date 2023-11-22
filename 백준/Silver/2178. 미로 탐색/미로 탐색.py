import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
lst = []
for i in range(n):
    lst.append(list(map(int, list(sys.stdin.readline().rstrip()))))
visited = [[1000000 for i in range(m)] for j in range(n)]
visited[0][0] = 1
dq = deque([(0, 0)])
while dq: 
    now = dq.popleft()
    row = [-1, 0, 0, 1]
    col = [0, -1, 1, 0]
    for i in range(4):
        nr = now[0] + row[i]
        nc = now[1] + col[i]
        visit = visited[now[0]][now[1]] + 1
        if 0 <= nr <= n-1 and 0 <= nc <= m-1:
            if lst[nr][nc] and visit < visited[nr][nc]:
                dq.append((nr, nc))
                visited[nr][nc] = visit
print(visited[n-1][m-1])