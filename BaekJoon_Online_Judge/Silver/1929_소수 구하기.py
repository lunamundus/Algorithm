# 문제 출처: https://www.acmicpc.net/problem/1929
# 에라토스테네스의 체 원리를 적용
# 시간 초과를 막기 위해 반복 횟수 및 최악의 상황 고려할 것

# ===== 내 풀이 ===== #
import sys

m, n = map(int, sys.stdin.readline().strip().split())

prime_nums = [True] * (n + 1)

prime_nums[0] = False
prime_nums[1] = False

re_n = int(n ** 0.5)

for i in range(2, re_n + 1):
    if prime_nums[i]:
        for j in range(i*2, n+1, i):
            prime_nums[j] = False

for x in range(m, n+1):
    if prime_nums[x]:
        print(x)