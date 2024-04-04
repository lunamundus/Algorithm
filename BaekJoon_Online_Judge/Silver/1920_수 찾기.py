# 문제 출처: https://www.acmicpc.net/problem/1920

# =================== #
'''
===== 문제 =====
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

===== 입력 =====
- 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다.
- 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
- 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.
- 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.
'''
# =================== #

# ===== 내 풀이 ===== #
## 시간초과 오류 발생

# n = int(input())
# numbers = list(map(int, input().split(' ')))

# m = int(input())
# check_numbers = list(map(int, input().split(' ')))

# for chk in check_numbers:
#     try:
#         numbers.index(chk)
#         print(1)
#     except:
#         print(0)
# =================== #
        
# ===== 내 풀이 ===== #
import sys

n = int(input())
numbers = list(map(int, sys.stdin.readline().split(' ')))
numbers.sort()

m = int(input())
check_numbers = list(map(int, sys.stdin.readline().split(' ')))

for chk in check_numbers:
    res = False
    start = 0
    end = n - 1
    
    while start <= end:
        mid = (start + end) // 2

        if numbers[mid] == chk:
            res = True
            break
        elif numbers[mid] < chk:
            start = mid + 1
        else:
            end = mid - 1
    
    if res == False:
        print(0)
    else:
        print(1)
    
# ===== 이진탐색 알고리즘 ===== #