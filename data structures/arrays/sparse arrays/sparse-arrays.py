from collections import defaultdict

strings = defaultdict(lambda: 0)
 
for _ in range(int(input().strip())):
    strings[input().strip()] += 1

for _ in range(int(input().strip())):
    print(strings[input().strip()])
