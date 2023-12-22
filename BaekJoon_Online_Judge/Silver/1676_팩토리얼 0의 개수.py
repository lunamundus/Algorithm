n = int(input())
res = 1

for i in range(1, n+1):
    res *= i

res = str(res)

zero_counter = 0
i = -1

while True:
    if res[i] != '0':
        break
    
    i -= 1
    zero_counter += 1
    
print(zero_counter)