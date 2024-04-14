import sys

n = int(sys.stdin.readline())

stack = []

for _ in range(n):
    data = list(sys.stdin.readline().rstrip().split(" "))

    command = data[0]

    if command == "push":
        value = data[1]
        stack.append(value)
    elif command == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(-1))
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])