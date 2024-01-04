# 요세푸스 문제 or 요세푸스 순열에 대해 정리해두기
# 내 풀이와 알고리즘을 이용한 풀이 둘 다 정리

# ==================== #
# 내 풀이

n, k = map(int, input().split())
num_list = [i for i in range(1, n+1)]
josephus = []

idx = 0
while True:
    if len(num_list) == 1:
        josephus.append(num_list.pop())
        break
    
    idx = idx + k - 1
    
    while idx > len(num_list) - 1:
        idx = idx - len(num_list)
    
    josephus.append(num_list.pop(idx))

print("<", end="")
for i in range(n-1):
    print(josephus[i], end=", ")
print(f"{josephus[n-1]}>")

# ==================== #
# 알고리즘 풀이