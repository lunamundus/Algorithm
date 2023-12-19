def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

n, k = map(int, input().split())

res = int(factorial(n) / (factorial(n-k) * factorial(k)))

print(res)

# ====================

# import math

# n, k = map(int, input().split())

# res = math.comb(n, k)

# print(res)