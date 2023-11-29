import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    ps = input().rstrip()
    stack = []
    for val in ps:
        if stack and val == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(val)
    if stack: print("NO")
    else: print("YES")