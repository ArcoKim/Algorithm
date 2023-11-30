import sys
input = sys.stdin.readline

while True:
    n = input().rstrip()
    if n == '.': break
    stack = []
    for val in n:
        if stack and ((val == ']' and stack[-1] == '[') or (val == ')' and stack[-1] == '(')):
            stack.pop()
        elif val in ('[', '(', ']', ')'):
            stack.append(val)
    if stack: print("no")
    else: print("yes")