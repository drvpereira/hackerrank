x1, v1, x2, v2 = map(int, input().strip().split(' '))
time = (x2 - x1)/(v1 - v2) if v1 != v2 else 0
    
if time > 0 and int(time) == time:
    print('YES')
else:
    print('NO')