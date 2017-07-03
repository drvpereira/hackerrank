for _ in range(int(input().strip())):
    s = input().strip()
    stack = []
    
    result = True
    for c in s:
        if c in [ '{', '[', '(' ]:
            stack.append(c)
        else:
            if len(stack) > 0:
                b_open = stack.pop()
                if c == '}' and b_open != '{' or c == ']' and b_open != '[' or c == ')' and b_open != '(':
                    result = False
                    break
            else:
                result = False
                break                
                
    print('YES' if result and len(stack) == 0 else 'NO')