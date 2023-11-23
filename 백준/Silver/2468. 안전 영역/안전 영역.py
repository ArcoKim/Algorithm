def dfs(y, x):
    stack = [(y, x)]
    while stack:
        yy,xx = stack.pop()
        memory[yy][xx] = 0
        yl = [-1, 0, 0, 1]
        xl = [0, -1, 1, 0]
        for i in range(4):
            ny = yy + yl[i]
            nx = xx + xl[i]
            if 0 <= ny < n and 0 <= nx < n and memory[ny][nx]:
                stack.append((ny,nx))

n = int(input())
field = []

mins = float('inf')
maxs = 0
for i in range(n):
    now = list(map(int, input().split()))
    mins = min(mins, min(now))
    maxs = max(maxs, max(now))
    field.append(now)

result = 0
for i in range(mins-1, maxs):
    memory = [[0 for i in range(n)] for j in range(n)]
    for j in range(n):
        for k in range(n):
            if field[j][k] > i:
                memory[j][k] = 1
    now = 0
    for j in range(n):
        for k in range(n):
            if memory[j][k]:
                dfs(j, k)
                now += 1
    result = max(result, now)

print(result)