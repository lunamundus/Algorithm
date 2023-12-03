alp_list = [0 for _ in range(26)] # A-Z

word = input().upper() # 입력값 대문자

# 알파벳 개수
for i in word:
    alp_list[ord(i)-65] += 1

# 최대값
max_value = max(alp_list)

alp_max = [i for i, v in enumerate(alp_list) if v == max_value]

# 동일한 최대 개수의 알파벳이 여러 개인지 판별
if len(alp_max) != 1:
    print("?")
else:
    print(chr(alp_max[0]+65))