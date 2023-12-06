N = int(input())
scores = list(map(int, input().split()))

M = max(scores)
res = 0

for i in scores:
    res += (i / M) * 100

print(res/N)