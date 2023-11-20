import sys
input = sys.stdin.readline

n,m = map(int, input().split())
num_dict = {}
str_dict = {}
for i in range(1, n+1):
    now = input().rstrip()
    num_dict[i] = now
    str_dict[now] = i

for _ in range(m):
    problem = input().rstrip()
    if problem.isnumeric():
        print(num_dict[int(problem)])
    else:
        print(str_dict[problem])