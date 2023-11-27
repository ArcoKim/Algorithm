n = int(input())
result = []
now = ''
for i in range(n):
    line = input()
    for j in range(len(line)):
        val = line[j]
        if val.isnumeric():
            now += val
        if now and (not val.isnumeric() or j == len(line)-1):
            result.append(int(now))
            now = ''
result.sort()
for val in result: print(val)