vowel = ['a', 'e', 'i', 'o', 'u']
while True:
    password = input()
    if password == "end": break
    count = [0, 0, 0]
    prev = ''
    flag = 0
    for val in password:
        if val in vowel:
            count[0] += 1
            count[1] = 0
            count[2] += 1
        else:
            count[0] = 0
            count[1] += 1
        if count[0] == 3 or count[1] == 3 or (val not in ('e', 'o') and val == prev):
            flag = 1
            break
        prev = val
    print(f"<{password}> is ", end='')
    if not count[2] or flag: print("not ", end='')
    print("acceptable.")