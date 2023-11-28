import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    mul = 5
    result = 0
    while mul <= n:
        result += n // mul
        mul *= 5
    print(result)