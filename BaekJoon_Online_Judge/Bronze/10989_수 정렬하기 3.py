# 계수 정렬(Counting Sort) 방식을 이용
    # 계수 정렬은 데이터가 양수 일 때
    # 데이터의 범위가 너무 크지 않을 때 (메모리 사이즈를 넘지 않을 때)

import sys

n = int(input())

count_list = [0 for _ in range(10001)]

for i in range(n):
    count_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    for j in range(count_list[i]):
        print(i)