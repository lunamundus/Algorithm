import sys

test_case = int(sys.stdin.readline().rstrip())

for _ in range(test_case):
    _str = sys.stdin.readline().rstrip()
    
    stack = []
    ans = "YES"
    
    for s in _str:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if len(stack) == 0:
                ans = "NO"
                break
            else:
                if stack.pop(-1) != "(":
                    ans = "NO"
                    break
        else:
            continue
        
    if len(stack) != 0:
        ans = "NO"
    
    print(ans)