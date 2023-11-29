import sys
input = sys.stdin.readline

def time_cal(old, new):
    if old[1] > new[1]:
        new[1] += 60
        new[0] -= 1
    result[winning][0] += new[0] - old[0]
    result[winning][1] += new[1] - old[1]
    if result[winning][1] >= 60:
        result[winning][1] -= 60
        result[winning][0] += 1

n = int(input())
point = [0, 0]
last = [[-1, -1], [-1, -1]]
result = [[0, 0], [0, 0]]
winning = -1
for i in range(n):
    win,time = input().split()
    win = int(win)-1
    mins,secs = map(int, time.split(':'))
    point[win] += 1
    if point[0] == point[1]:
        time_cal(last[winning], [mins, secs])
        last[winning] = [-1, -1]
        winning = -1
    elif winning == -1:
        last[win] = [mins, secs]
        winning = win
if winning != -1:
    time_cal(last[winning], [48, 0])
print(f"{result[0][0]:02}:{result[0][1]:02}")
print(f"{result[1][0]:02}:{result[1][1]:02}")