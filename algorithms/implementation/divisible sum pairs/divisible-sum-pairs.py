n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
total = 0

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if (a[i] + a[j]) % k == 0:
            total += 1

print(total)