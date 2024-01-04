n = int(input())
coor_list = [tuple(map(int, input().split())) for _ in range(n)]

coor_list.sort(key=lambda x: (x[1], x[0]))

for i in range(n):
    print(*coor_list[i])