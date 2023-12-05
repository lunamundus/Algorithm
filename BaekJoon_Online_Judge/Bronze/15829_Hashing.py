l = int(input())
s = input()

hashing_res = 0

for i in range(l):
    hashing_res += ((ord(s[i])-96) * pow(31, i))
    
hashing_res = hashing_res % 1234567891
    
print(hashing_res)

####################################

# def myHashing(chars):
#     R = 31
#     M = 1234567891
    
#     # 알파벳을 숫자로 변경
#     nums = []
#     for i in range(len(chars)):
#         nums.append(ord(chars[i]) - 96)
        
#     # Hashing
#     h_nums = []
#     for i in range(len(nums)):
#         h_nums.append(nums[i] * (R ** i))
        
#     h_sum = sum(h_nums)
#     hashing_res = h_sum % M
    
#     return hashing_res
    
# l = int(input())
# s = input()

# chars = list(s)

# print(myHashing(chars))