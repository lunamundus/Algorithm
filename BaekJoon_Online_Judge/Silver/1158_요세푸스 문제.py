# 백준 11866번과 같은 문제
# 다만 11866번 문제는 N의 범위가 1 ~ 1000까지이며, 1158번 문제는 1 ~ 5000까지
# 메모리 및 시간 제한의 주의가 조금 더 필요하다
# 같은 풀이로 풀이 성공

# ==================== #
# 내 풀이 1
# 반복문과 인덱스를 이용하여 처리
# 기존 리스트에서 .pop() 메서드를 이용하여 원소를 제거하며 처리

n, k = map(int, input().split())
num_list = [i for i in range(1, n+1)]
josephus = []

idx = 0
while True:
    # 마지막 한명 남았을 때, 마지막 원소 추가 후 반복 종료
    if len(num_list) == 1:
        josephus.append(num_list.pop())
        break
    
    # 다음 인덱스 결정
    idx = idx + k - 1
    
    # 다음 인덱스가 리스트 길이보다 긴 경우 처리
    while idx > len(num_list) - 1:
        idx = idx - len(num_list)
    
    # 해당하는 인덱스의 원소 추가
    josephus.append(num_list.pop(idx))

# 형식에 맞게 출력
print("<" + str(josephus)[1:-1] + ">")

# print("<", end="")
# for i in range(n-1):
#     print(josephus[i], end=", ")
# print(f"{josephus[n-1]}>")

# ==================== #
# 내 풀이 2

# n, k = map(int, input().split())
# num_list = [i for i in range(1, n+1)]

# idx = 0
# print("<", end="")
# while True:
#     if len(num_list) == 1:
#         print(num_list.pop(), end="")
#         break
    
#     idx = idx + k - 1
    
#     while idx > len(num_list) - 1:
#         idx = idx - len(num_list)
    
#     print(num_list.pop(idx), end=", ")

# print(">")

# ==================== #
# 알고리즘 풀이