rem = []

for i in range(10):
    num = int(input())
    rem.append(num%42)
    
rem = set(rem)

print(len(rem))