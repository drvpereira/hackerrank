n = int(input().strip())
result = set(map(chr, range(ord('a'), ord('z')+1)))
for _ in range(n):
    result = result.intersection(set(input().strip()))
print(len(result))
