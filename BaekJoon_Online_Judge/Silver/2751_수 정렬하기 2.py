# ============================ #
# 실패 : 시간초과

n = int(input())

count_list = [0 for _ in range(1000001)]

for i in range(n):
    num = int(input())
    count_list[num] += 1

for idx, value in enumerate(count_list):
    if value == 1:
        print(idx)

# ============================ #
# 실패 : 시간초과
# 파이썬 내장 함수인 sorted를 이용하는 것은 시간초과에 걸리는 듯...

# n = int(input())

# num_list = [int(input()) for _ in range(n)]

# num_list = sorted(num_list)

# for i in num_list:
#     print(i)