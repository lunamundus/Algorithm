while True:
    _str = input()
    
    stack = []
    ans = 'yes'
    
    if _str == '.':
        break
    
    for s in _str:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if len(stack) == 0:
                ans = 'no'
                break
            else:
                if stack.pop(-1) != '(':
                    ans = 'no'
                    break
        elif s == ']':
            if len(stack) == 0:
                ans = 'no'
                break
            else:
                if stack.pop(-1) != '[':
                    ans = 'no'
                    break
        else:
            continue
        
    if len(stack) != 0:
        ans = 'no'
    
    print(ans)