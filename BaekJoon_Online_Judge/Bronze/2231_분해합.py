N = int(input())

for num in range(N):
    res = str(num)
    res_sum = num
    
    for i in res:
        res_sum += int(i)
        
    if res_sum == N:
        break

if res_sum == N:
    print(int(res))
else:
    print(0)