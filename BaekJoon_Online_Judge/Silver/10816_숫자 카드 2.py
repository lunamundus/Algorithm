import sys

n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline().rstrip())
m_nums = list(map(int, sys.stdin.readline().rstrip().split()))

hashmap = {}
for i in nums:
    if i in hashmap:
        hashmap[i] += 1
    else:
        hashmap[i] = 1

for j in m_nums:
    if j in hashmap:
        print(hashmap[j], end=" ")
    else:
        print(0, end=" ")