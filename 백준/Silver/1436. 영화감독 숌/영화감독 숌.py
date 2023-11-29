import sys
input = sys.stdin.readline

n = int(input())
result = 665
i = 0
while i < n:
    result += 1
    if "666" in str(result):
        i += 1

print(result)