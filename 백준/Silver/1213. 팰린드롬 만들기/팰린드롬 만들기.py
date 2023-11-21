name = input()

name_cnt = {}
for val in name:
    if val in name_cnt:
        name_cnt[val] += 1
    else:
        name_cnt[val] = 1

front = ""
mid = ''
back = ""
flag = 0
for key in sorted(name_cnt):
    if name_cnt[key] % 2 == 1 and (len(name) % 2 == 0 or mid):
        flag = 1
        break
    if name_cnt[key] % 2 == 1 and len(name) % 2 == 1:
        mid = key
    front += key * (name_cnt[key] // 2)
    back = key * (name_cnt[key] // 2) + back

if flag: print("I'm Sorry Hansoo")
else: print(front + mid + back)