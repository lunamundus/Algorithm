T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    
    floor = N % H
    number = N // H + 1
    
    if floor == 0:
        floor = H
        number = N // H
    
    room_number = str(floor) + str(number).zfill(2)
    
    print(room_number)


'''
.zfill(n) 메소드는 n(자릿수)의 값만큼 자릿수를 0으로 채워줌
'3'.zfill(2) -> '03'
'5'.zfill(3) -> '005'

floor의 값이 0이 나오는 경우, 즉 나머지가 0일 때를 고려해야 함
'''