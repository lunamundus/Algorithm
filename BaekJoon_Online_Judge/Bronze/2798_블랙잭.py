N, M = map(int, input().split())
cards = list(map(int, input().split()))

res = 0
val_error = 300000

for i in range(len(cards)-2):
    a = cards[i]
    
    if a > M:
        continue
    
    for j in range(i+1, len(cards)-1):
        b = cards[j]
        
        if a + b > M:
            continue
        
        for k in range(j+1, len(cards)):
            c = cards[k]
            temp = a + b + c
            
            if temp <= M:
                if M-temp < val_error:
                    val_error = M - temp
                    res = temp

print(res)