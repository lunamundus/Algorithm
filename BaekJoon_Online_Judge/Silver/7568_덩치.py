# 덩치 등수 = 본인보다 덩치가 큰 사람이 몇명 있는가로 결정
# 덩치 등수 = 누적 등수의 개념이 아님
# "덩치가 크다"라는 것은 몸무게와 키가 모두 커야함

n = int(input())
p_list = [tuple(map(int, input().split())) for _ in range(n)]
score = [0 for _ in range(n)]

for i in range(n):
    count = 1
    for j in range(n):
        if i == j:
            continue
        
        if (p_list[i][0] < p_list[j][0]) and (p_list[i][1] < p_list[j][1]):
            count += 1
    
    score[i] = count
    
print(*score)