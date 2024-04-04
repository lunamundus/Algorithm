# 문제 출처: https://www.acmicpc.net/problem/10815
# 백준 1920.수 찾기 문제와 동일하게 이진탐색 방법을 이용하여 풀이 가능

# ===== 내 풀이 ===== #
import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split(' ')))
numbers.sort()

m = int(sys.stdin.readline())
check_numbers = list(map(int, sys.stdin.readline().split(' ')))

result = []

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
    
    if res:
        result.append(1)
    else:
        result.append(0)
        
print(*result)