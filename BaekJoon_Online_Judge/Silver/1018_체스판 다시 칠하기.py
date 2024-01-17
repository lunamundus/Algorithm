n, m = map(int, input().split())

board = [input() for _ in range(n)]

result = []

for i in range(n - 7):
    for j in range(m - 7):
        count1 = 0 # 시작이 Black 일 때
        count2 = 0 # 시작이 White 일 때
        
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b)%2 == 0:
                    if board[a][b] != 'B': # 시작이 Black인데 Black이 아닌 경우
                        count1 += 1
                    if board[a][b] != 'W': # 시작이 White인데 White가 아닌 경우
                        count2 += 1
                else:
                    if board[a][b] != 'W': # 시작이 Black인데 Black 옆에 White가 아닌 경우
                        count1 += 1
                    if board[a][b] != 'B': # 시작이 White인데 White 옆에 Black이 아닌 경우
                        count2 += 1
        
        result.append(count1)
        result.append(count2)
        
print(min(result))