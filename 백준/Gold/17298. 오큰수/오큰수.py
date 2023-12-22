import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

result = [-1 for _ in range(n)]
stack = []
for i in range(n):
    val = a[i]
    while stack and stack[-1][0] < val:
        result[stack.pop()[1]] = val
    stack.append((val, i))

print(*result)