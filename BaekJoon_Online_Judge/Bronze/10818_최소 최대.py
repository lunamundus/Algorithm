# n = int(input())
# nums = list(map(int, input().split()))

# print(f"{min(nums)} {max(nums)}")

n = int(input())
nums = list(map(int, input().split()))

max_num = -1000000
min_num = 1000000

for i in range(n):
    if nums[i] > max_num:
        max_num = nums[i]
    
    if nums[i] < min_num:
        min_num = nums[i]
        
print(f"{min(nums)} {max(nums)}")