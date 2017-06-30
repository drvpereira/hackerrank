input()
arr = list(map(int, input().strip().split(' ')))
result = [ arr[i] for i in reversed(range(len(arr))) ]
print(*result)