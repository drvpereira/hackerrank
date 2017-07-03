n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

result = float('-inf')
for i in range(n):
    number = a[i]
    total = 0
    for j in range(n):
        if number == a[j] or number == a[j] + 1:
            total += 1
    result = max(result, total)
    
print(result)