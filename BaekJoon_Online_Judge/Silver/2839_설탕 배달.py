# 문제 출처: https://www.acmicpc.net/problem/2839

# ===== 풀이 ===== #
import sys

n = int(sys.stdin.readline())

res_list = []
x = 0
while 3 * x <= n:
    if (n - (3 * x)) % 5 == 0:
        temp_res = int((n - (3 * x)) // 5 + x)
        res_list.append(temp_res)
    
    x = x + 1
    
if len(res_list) == 0:
    print(-1)
else:
    print(min(res_list))