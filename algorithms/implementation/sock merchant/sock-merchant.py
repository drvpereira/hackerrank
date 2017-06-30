from collections import defaultdict

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
by_color = defaultdict(int)
total = 0

for item in a:
    by_color[item] += 1
for item in by_color:
    total += by_color[item] // 2
    
print(total)