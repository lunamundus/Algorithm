T = int(input()) # 테스트 케이스 입력

for i in range(T):
    R, S = input().split() # R과 S 입력
    R = int(R) # R을 String -> int 변환
    
    res = ''
    
    for j in range(len(S)):
        res += (S[j] * R)
        
    print(res)