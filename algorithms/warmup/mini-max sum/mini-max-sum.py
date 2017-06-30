arr = list(map(int, input().strip().split(' ')))
total = sum(arr)
print(total - max(arr), total - min(arr))