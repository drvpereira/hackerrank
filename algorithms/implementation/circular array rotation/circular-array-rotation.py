n, k, q = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
for _ in range(q):
    m = int(input().strip())
    print(a[(n - k + m) % n])