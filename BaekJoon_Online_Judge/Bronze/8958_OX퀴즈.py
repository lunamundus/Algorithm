T = int(input())

for i in range(T):
    answers = input()
    score = 1
    res = 0
    
    for ans in answers:
        if ans == 'O':
            res += score
            score += 1
        else:
            score = 1
            
    print(res)