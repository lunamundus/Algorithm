# 출처: https://www.acmicpc.net/problem/2108

# collections 라이브러리의 Counter 함수 정리

# ===== 풀이 ===== #
import sys
from collections import Counter

# 함수 정의
def num_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    elif num - int(num) <= -0.5:
        return int(num) - 1
    else:
        return int(num)

def _avg(nums, n):
    sum_of_nums = 0
    for num in nums:
        sum_of_nums += num
    avg = sum_of_nums / n
    avg = num_round(avg)
    return avg

def _mid(nums, n):
    n = n // 2
    return nums[n]

def _mode(nums):
    a = Counter(nums)
    mode_value = a.most_common()
    if list(a.values()).count(max(a.values())) >= 2:
        return a.most_common()[1][0]
    else:
        return a.most_common()[0][0]
    
def _range(nums):
    if len(nums) == 1:
        return 0
    else:
        return max(nums) - min(nums)

# 실행 코드
n = int(sys.stdin.readline())

nums = [int(sys.stdin.readline()) for _ in range(n)]
nums.sort()

print(_avg(nums, n))
print(_mid(nums, n))
print(_mode(nums))
print(_range(nums))