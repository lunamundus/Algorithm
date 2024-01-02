# O(nlogn)의 시간복잡도를 가진 정렬 알고리즘을 사용해야 함
# 퀵 정렬의 경우 평균 시간복잡도는 O(nlogn)의 시간복잡도를 가지지만 최악의 경우 O(n^2)의 시간복잡도를 가짐
# 병합정렬과 힙정렬의 경우 최악의 경우에도 O(nlogn)의 시간복잡도를 가짐
# 따라서 병합정렬 혹은 힙정렬을 사용해야 함
# (파이썬 내장함수인 sorted() 함수 혹은 .sort() 메소드는 퀵 정렬의 알고리즘으로 이루어져 있음)

# ============================ #
# 병합정렬 알고리즘
import sys

def merge_sort(num_list):
    if len(num_list) < 2:
        # 리스트의 길이가 1개면 리스트 반환
        return num_list
    
    # 리스트의 중간을 기준으로 리스트 분할
    mid = len(num_list) // 2
    low_list = merge_sort(num_list[:mid])
    high_list = merge_sort(num_list[mid:])
    
    merge_list = []
    l = h = 0
    
    while l < len(low_list) and h < len(high_list):
        if low_list[l] < high_list[h]:
            merge_list.append(low_list[l])
            l += 1
        else:
            merge_list.append(high_list[h])
            h += 1
            
    merge_list += low_list[l:]
    merge_list += high_list[h:]
    
    return merge_list

n = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline()) for _ in range(n)]

sorted_list = merge_sort(num_list)

for i in sorted_list:
    print(i)

# ============================ #
# 힙(Heap) 정렬 알고리즘


# ============================ #
# 파이썬 내장 함수 sorted 사용
# import sys

# n = int(sys.stdin.readline())
# num_list = [int(sys.stdin.readline()) for _ in range(n)]

# sorted_list = sorted(num_list)

# for i in sorted_list:
#     print(i)

# ============================ #
# 실패 : 시간초과

# n = int(input())

# count_list = [0 for _ in range(1000001)]

# for i in range(n):
#     num = int(input())
#     count_list[num] += 1

# for idx, value in enumerate(count_list):
#     if value == 1:
#         print(idx)

# ============================ #
# 실패 : 시간초과
# 파이썬 내장 함수인 sorted를 이용하는 것은 시간초과에 걸리는 듯...

# n = int(input())

# num_list = [int(input()) for _ in range(n)]

# num_list = sorted(num_list)

# for i in num_list:
#     print(i)