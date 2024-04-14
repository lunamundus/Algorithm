import sys

n = int(sys.stdin.readline())

deque = []

for _ in range(n):
    data = list(sys.stdin.readline().rstrip().split(" "))

    command = data[0]

    if command == "push_front":
        value = data[1]
        deque.insert(0, value)

    elif command == "push_back":
        value = data[1]
        deque.insert(len(deque), value)

    elif command == "pop_front":
        if deque:                           # 덱에 정수가 있는 경우
            print(deque[0])
            del deque[0]
        else:                               # 덱에 정수가 없는 경우
            print(-1)

    elif command == "pop_back":
        if deque:
            print(deque.pop(-1))
        else:
            print(-1)

    elif command == "size":
        print(len(deque))

    elif command == "empty":
        if deque:
            print(0)
        else:
            print(1)
    
    elif command == "front":
        if deque:
            print(deque[0])
        else:
            print(-1)

    elif command == "back":
        if deque:
            print(deque[-1])
        else:
            print(-1)