n = int(input().strip())
a = list(map(int, input().strip().split()))
p = { val : idx + 1 for idx, val in enumerate(a)}

for i in range(n):
    print(p[p[i+1]])