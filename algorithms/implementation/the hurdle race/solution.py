n, k = map(int, input().strip().split(' '))
height = list(map(int, input().strip().split(' ')))

result = 0
for hurdle in height:
    result += max(0, hurdle - k)
    k = max(k, hurdle)

print(result)