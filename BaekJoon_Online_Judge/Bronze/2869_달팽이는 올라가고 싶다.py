a, b, v = map(int, input().split())

# 하루동안 이동하는 거리
day_up = a - b

# 마지막 전날까지 올라가야 하는 거리
remain_v = v - a

# 지난 시간
if remain_v % (a-b) == 0:
    days = remain_v // (a - b) + 1
else:
    days = remain_v // (a - b) + 2

print(days)