n,m = map(int, input().split())
j = int(input())
apples = [int(input()) for _ in range(j)]
prev = 1

result = 0
for apple in apples:
    if apple < prev:
        result += prev - apple
        prev = apple
    elif prev+m-1 < apple:
        result += apple - (prev+m-1)
        prev = apple-m+1

print(result)