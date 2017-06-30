stack, maxes = [], []
for _ in range(int(input())):
    query = list(map(int, input().split(' ')))
    
    if query[0] == 1:
        elem = query[1]
        stack.append(elem)
        if len(maxes) == 0 or elem >= maxes[-1]:
            maxes.append(elem)
    elif query[0] == 2:
        elem = stack.pop()
        if maxes[-1] == elem:
            maxes.pop()
    else:
        print(maxes[-1])