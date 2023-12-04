# 등차수열을 이용하여 계산
# an = 1 + sum(bn-1)

def a_sequence(n):
    x = 3*pow(n, 2) - 3*n + 1
    return x

N = int(input())

a = 0
b = 0

if N == 1:
    print(1)

for i in range(1, N):
    a = a_sequence(i)
    b = a_sequence(i+1)
    
    if (N > a) & (N <= b):
        print(i+1)
        break