n = int(input())
bar = list(map(int, input().split(' ')))
d, m = map(int, input().split(' '))
i, total = 0, 0

while i + m <= n:
    if sum(bar[i:i+m]) == d:
        total += 1
    i += 1
print(total)
