hour, minute = map(int, input().split())

if minute >= 45:
    print(f"{hour} {minute-45}")
else:
    if hour != 0:
        print(f"{hour-1} {minute+15}")
    else:
        print(f"{23} {minute+15}")
        
'''
우리가 시간 계산을 할 때 사용하는 방법을 그대로 사용
- minute이 45보다 크면, hour는 입력값 그대로 출력, minute은 입력값에서 45를 뺀 값을 출력
- minute이 45보다 작으면,
    - hour가 0이 아닐 떈, hour는 입력값에서 1을 빼고 출력하고, minute은 입력값에서 15를 더한 값을 출력(why? 1시간은 60분이고, 60분에서 45분을 빼면 15분이 남기 때문)
    - hour가 0일 때, hour는 23을 출력(why? hour가 0일땐 0시이기 때문에 여기서 1시간을 빼면 23시가 됨)하고, minute은 입력값에서 15를 더한 값을 출력
'''