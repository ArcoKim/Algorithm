a,b,c = map(int, input().split())

memory = {1: a % c}

def cal(mul):
    if mul in memory:
        return memory[mul]
    second = mul // 2
    if mul % 2 == 1: second += 1
    memory[mul] = cal(mul // 2) * cal(second) % c
    return memory[mul]

cal(b)
print(memory[b])