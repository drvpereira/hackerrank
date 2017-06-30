int(input())
a = list(map(int, input().split()))
print([ a.count(v) for v in range(100) ].index(1))