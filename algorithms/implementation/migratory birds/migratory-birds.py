n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
flock = { type : types.count(type) for type in range(1,6) }
print(max(flock, key = lambda key : flock[key]))