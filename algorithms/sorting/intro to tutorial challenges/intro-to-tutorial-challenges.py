v = int(input())
n = int(input())
ar = list(map(int, input().split()))

for idx, itm in enumerate(ar):
    if (itm == v):
        print(idx)
        break