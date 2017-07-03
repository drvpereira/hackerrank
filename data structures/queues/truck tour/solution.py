result = 0
weight = 0
for i in range(int(input())):
    p, d = map(int, input().strip().split())
    weight += p - d    
    if weight < 0:
        result = i + 1
        weight = 0
print(result)