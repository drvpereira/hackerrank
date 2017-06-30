list = sorted([ input().strip() for _ in range(int(input().strip()))], key = lambda x: (len(x), x))
print('\n'.join(map(str, list)))
