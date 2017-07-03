t = int(input().strip())
for _ in range(t):
    n, m, s = map(int, input().strip().split(' '))
    result = (s + m - 1) % n
    print(result if result > 0 else n)
