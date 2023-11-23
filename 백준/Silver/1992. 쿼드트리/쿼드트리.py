import sys

def zip(lst):
    global result
    now = lst[0][0]
    exits = True
    for i in lst:
        for j in i:
            if now != j:
                exits = False
                break
    if exits: result += now
    else:
        result += '('
        limit = len(lst) // 2
        for i in range(0, len(lst), limit):
            for j in range(0, len(lst), limit):
                zip([row[j:j+limit] for row in lst[i:i+limit]])
        result += ')'

n = int(sys.stdin.readline())
lst = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
result = ""
zip(lst)
print(result)