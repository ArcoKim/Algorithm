h,w = map(int, input().split())
cloud = [list(input()) for _ in range(h)]

for i in range(h):
    loc = -1
    flag = 0
    for j in range(w):
        if flag:
            loc += 1
        if cloud[i][j] == 'c':
            loc = 0
            flag = 1
        print(loc, end=' ')
    print()