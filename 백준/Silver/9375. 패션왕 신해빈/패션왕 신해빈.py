t = int(input())

for i in range(t):
    n = int(input())

    wears = {}
    for i in range(n):
        name,wear = input().split()
        if wear in wears:
            wears[wear] += 1
        else:
            wears[wear] = 1

    result = 1
    for val in wears.values():
        result *= val + 1

    print(result - 1)