import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque([(0,0)])
    visited = [[0 for i in range(m)] for j in range(n)]
    visited[0][0] = 1
    while queue:
        y,x = queue.popleft()
        yl = [-1, 0, 0, 1]
        xl = [0, -1, 1, 0]
        for i in range(4):
            ny = y + yl[i]
            nx = x + xl[i]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                visited[ny][nx] = 1
                if cheese[ny][nx] == 1:
                    global count
                    count -= 1
                    cheese[ny][nx] = 0
                else:
                    queue.append((ny,nx))

n,m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]

count = sum(x.count(1) for x in cheese)
result = 0
last = 0
while count > 0:
    result += 1
    last = count
    bfs()

print(result)
print(last)