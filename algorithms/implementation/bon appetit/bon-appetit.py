n, k = map(int, input().split(' '))
items = list(map(int, input().split(' ')))
b = int(input())
result = b - (sum(items) - items[k]) // 2
if result == 0:
    print('Bon Appetit')
else:
    print(result)
    