n = int(input())
xy_list = [tuple(map(int, input().split())) for _ in range(n)]

xy_list.sort(key=lambda x: (x[0], x[1]))

for i in range(n):
    print(*xy_list[i])