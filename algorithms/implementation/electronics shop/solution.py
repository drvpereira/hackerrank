s, n, m = map(int, input().strip().split(' '))
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))

total = -1
for kb in keyboards:
    for drive in drives:
        value = kb + drive
        if value > total and value <= s:
            total = value

print(total)