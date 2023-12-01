import sys
input = sys.stdin.readline

def dfs(node):
    if par[node] != -1 and node in tree[par[node]]:
        tree[par[node]].remove(node)
    while tree[node]:
        child = tree[node].pop()
        dfs(child)
    del tree[node]

n = int(input())
par = list(map(int, input().split()))
tree = {}

for i in range(len(par)):
    val = par[i]
    if val != -1:
        if val not in tree:
            tree[val] = []
        tree[val].append(i)
    if i not in tree:
        tree[i] = []

dfs(int(input()))
print(sum(not tree[node] for node in tree))