n = int(input())

check_num = '666'
check_count = 0
num = 666

while True:
    if check_num in str(num):
        check_count += 1
    
    if check_count == n:
        break
        
    num += 1

print(num)