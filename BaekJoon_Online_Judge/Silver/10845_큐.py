import sys

n = int(sys.stdin.readline())

queue = []

for _ in range(n):
    data = list(sys.stdin.readline().rstrip().split(" "))

    command = data[0]

    if command == "push":
        value = data[1]
        queue.append(value)
    elif command == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif command == "size":
        print(len(queue))
    elif command == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])