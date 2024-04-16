# 문제 출처: https://www.acmicpc.net/problem/18110

"""
python의 round 함수 조심
python의 round 함수는 반올림할 때 사용하지만, Bankers' Rounding 형식을 따르기 때문에 .5에 가까운 짝수로 반올림 함
round(1.5)와 round(2.5)는 둘다 2를 반환함

--> 따라서 본 문제에서는 round 함수를 사용하면 오류가 발생함
"""

# ===== 내 풀이 ===== #
import sys

def num_round(number):
    if number - int(number) >= 0.5:
        return int(number) + 1
    else:
        return int(number)

def calc_score(n, scores):
    cut_qty = int(num_round(n * 0.15))

    if cut_qty == 0:
        pb_score = int(num_round(sum(scores) / len(scores)))
    else:
        pb_score = int(num_round(sum(scores[cut_qty:-cut_qty]) / len(scores[cut_qty:-cut_qty])))

    return pb_score


n = int(sys.stdin.readline().rstrip())

if n == 0:
    print(0)
else:
    scores = []
    for _ in range(n):
        score = int(sys.stdin.readline().rstrip())
        scores.append(score)

    scores.sort()
    res = calc_score(n, scores)
    print(res)