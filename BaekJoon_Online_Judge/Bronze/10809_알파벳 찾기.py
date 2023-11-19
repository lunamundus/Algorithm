from string import ascii_lowercase

alph_list = list(ascii_lowercase)
res = [-1 for _ in range(26)]

word = input()

for idx, alph in enumerate(alph_list):
    if alph in word:
        res[idx] = word.index(alph)

print(*res)



'''
from string import ascii_lowercase : 알파벳 소문자 [a-z]
from string import ascii_uppercase : 알파벳 대문자 [A-Z]
from string import ascii_letters : 알파벳 [a-z, A-Z]
'''