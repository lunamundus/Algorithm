import sys

k = int(sys.stdin.readline().rstrip())

nums = []

for _ in range(k):
    number = int(sys.stdin.readline().rstrip())
    
    if number == 0:
        nums.pop(-1)
        continue
    
    nums.append(number)
        
print(sum(nums))