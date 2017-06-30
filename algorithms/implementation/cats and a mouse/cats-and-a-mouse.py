for _ in range(int(input().strip())):
    x, y, z = map(int, input().strip().split(' '))
    diff_a = abs(x - z)
    diff_b = abs(y - z)
    if diff_a < diff_b:
        print('Cat A')
    elif diff_b < diff_a:
        print('Cat B')
    else:
        print('Mouse C')