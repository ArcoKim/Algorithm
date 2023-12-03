import sys
from collections import deque
input = sys.stdin.readline

def bfs(a):
    num = 1
    queue = deque([a])
    visited = [0 for _ in range(n+1)]
    visited[a] = 1

    while queue:
        now = queue.popleft()
        for val in dep[now]:
            if not visited[val]:
                num += 1
                visited[val] = 1
                queue.append(val)

    return num

n,m = map(int, input().split())
dep = {x:[] for x in range(1,n+1)}
for _ in range(m):
    a,b = map(int, input().split())
    dep[b].append(a)

maxs = 0
result = []
for i in range(1,n+1):
    ret = bfs(i)
    if ret > maxs:
        maxs = ret
        result = [i]
    elif ret == maxs:
        result.append(i)

print(*result)