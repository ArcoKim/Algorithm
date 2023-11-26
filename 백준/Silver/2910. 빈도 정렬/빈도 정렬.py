n,c = map(int, input().split())
msg = list(map(int, input().split()))

count = {}
order = 1
for num in msg:
    if num in count:
        count[num][0] += 1
    else:
        count[num] = [1, order]
        order += 1

sorted_count = sorted(count.items(), key=lambda item: (-item[1][0], item[1][1]))
for pair in sorted_count:
    print(f'{pair[0]} ' * pair[1][0], end='')