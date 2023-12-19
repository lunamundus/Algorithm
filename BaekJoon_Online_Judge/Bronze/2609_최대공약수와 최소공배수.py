# 최대공약수
def gcd(a, b):
    # 유클리드 호제법 알고리즘
    # 소스코드로 구현할 떄는 a, b의 크기를 고려하지 않아도
    # 계산 과정 중에서 a에는 큰 수가, b에는 작은수가 위치함
    while b != 0:
        a, b = b, a % b
    
    return a

a, b = map(int, input().split())

gcd_num = gcd(a, b)

print(gcd_num)
# 최소공배수는 두 수의 곱을 최대공약수로 나눈 것
print(int(a * b // gcd_num))