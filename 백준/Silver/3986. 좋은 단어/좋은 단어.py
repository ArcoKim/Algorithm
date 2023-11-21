n = int(input())

result = 0
for i in range(n):
    word = input()
    stack = []
    for val in word:
        if stack and stack[-1] == val:
            stack.pop()
        else:
            stack.append(val)
    if not stack:
        result += 1

print(result)