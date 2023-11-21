n = int(input())
m = int(input())
ingr = set(map(int, input().split()))

result = 0
while ingr:
    now = ingr.pop()
    if m - now in ingr:
        ingr.remove(m - now)
        result += 1

print(result)