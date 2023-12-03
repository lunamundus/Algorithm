N = int(input())
nums = list(map(int, input().split()))

count = 0

for i in range(N):
    if nums[i] == 1:
        continue
    elif nums[i] == 2:
        count += 1
        continue
    else:
        for j in range(2, nums[i]):
            if nums[i] % j == 0:
                break
        if j+1 == nums[i]:
            count += 1

print(count)