# 문제 출처: https://www.acmicpc.net/problem/2161
# 유사 문제: 2164. 카드2 https://www.acmicpc.net/problem/2164

# ===== 풀이 ===== #
import sys

n = int(sys.stdin.readline())
card = [_ for _ in range(1, n+1)]

rm_card = []

while True:
    if len(card) == 1:
        break
    
    rm_card.append(card.pop(0))
    temp = card.pop(0)
    card.append(temp)

res = rm_card + card
print(*res)