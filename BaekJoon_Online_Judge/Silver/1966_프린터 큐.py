# 문제 출처: https://www.acmicpc.net/problem/1966
# max(arr, key) 함수를 이용한 최대값 찾기

# === 내 풀이 === #
import sys

cases = int(sys.stdin.readline())

for case in range(cases):
    n, m = map(int, sys.stdin.readline().strip().split())
    doc_list = list(map(int, sys.stdin.readline().strip().split()))

    doc_list = [(idx, doc) for idx, doc in enumerate(doc_list)]

    count = 1
    while True:
        if doc_list[0] == max(doc_list, key=lambda x:x[1]):
            if doc_list[0][0] == m:
                print(count)
                break
            doc_list.pop(0)
            count +=1
        else:
            doc_list.append(doc_list.pop(0))