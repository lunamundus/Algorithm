# ============================ #
# 성공 :  파이썬 내장 sorted 함수 이용

# 입력
n = int(input())
words = [input() for _ in range(n)]

# 중복 제거
words = list(set(words))

# 정렬
words = sorted(words) # 오름차순 정렬
words = sorted(words, key=len) # 길이 순 정렬

# 출력
for word in words:
    print(word)

# ============================ #
# 실패 : 시간초과
# 버블 정렬로는 절대 불가능한 듯

# # 입력
# n = int(input())
# words = [input() for _ in range(n)]

# # 중복 제거
# words = list(set(words))

# # (len, word)를 쌍으로 갖는 list 생성
# len_words = []

# for i in range(len(words)):
#     len_words.append((len(words[i]), words[i]))
    
# # 정렬
# for i in range(len(len_words)-1):
#     for j in range(i+1, len(len_words)):
#         if len_words[i][0] > len_words[j][0]:
#             len_words[i], len_words[j] = len_words[j], len_words[i]
#         else:
#             if len_words[i][0] == len_words[j][0]:
#                 if len_words[i][1] > len_words[j][1]:
#                     len_words[i], len_words[j] = len_words[j], len_words[i]

# # 출력
# for word in len_words:
#     print(word[1])

# ============================ #
# 실패 : 시간초과

# # 입력
# n = int(input())
# words = [input() for _ in range(n)]
    
# # 중복 제거 
# words = list(set(words))

# # 글자 수 정렬
# for i in range(len(words)-1):
#     for j in range(i+1, len(words)):
#         if len(words[i]) > len(words[j]):
#             words[i], words[j] = words[j], words[i]

# # 알파벳 정렬
# for i in range(len(words)-1):
#     for j in range(i+1, len(words)):
#         if len(words[i]) != len(words[j]):
#             break
#         if words[i] > words[j]:
#             words[i], words[j] = words[j], words[i]
        
# # 출력
# for word in words:
#     print(word)