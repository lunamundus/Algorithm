max_num, idx = 0, 0

for i in range(9):
    x = int(input())
    
    if x > max_num:
        max_num = x
        idx = i+1

print(max_num)
print(idx)