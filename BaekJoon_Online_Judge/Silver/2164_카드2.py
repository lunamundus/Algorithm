# 문제 출처: https://www.acmicpc.net/problem/2164
# 유사 문제: 2161.카드1 https://www.acmicpc.net/problem/2161

# ===== 풀이 ===== #
import sys

n = int(sys.stdin.readline())
card = [_ for _ in range(1, n+1)]

while True:
    if len(card) == 1:
        break
    
    if len(card) % 2 == 0:
        del card[0:len(card):2]
    else:
        del card[0:len(card):2]
        temp = card.pop(0)
        card.append(temp)

print(card[0])