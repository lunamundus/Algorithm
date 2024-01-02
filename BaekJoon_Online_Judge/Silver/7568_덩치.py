import sys

n = int(sys.stdin.readline())

weight = []
height = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    weight.append(x)
    height.append(y)
    
weight_copy = weight.copy()
score = [0 for _ in range(n)]
score_value = 1

while 0 in score:
    max_weight = max(weight_copy)
    weight_copy.remove(max_weight)
    
    max_index = weight.index(max_weight)
    score[max_index] = score_value
    count = 1
    
    for i in range(len(weight)):
        if i == max_index:
            continue
        
        if (weight[i] <= max_weight) and (height[i] >= height[max_index]):
            score[i] = score_value
            weight_copy.remove(weight[i])
            count += 1
    
    if count != 1:
        score_value += count
    else:
        score_value += 1
    
print(*score)