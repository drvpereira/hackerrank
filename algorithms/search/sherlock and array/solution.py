def condition_satisfies(a, start, end):
    m = start + ((end - start) // 2)
    l = sum(a[:m])
    r = sum(a[m+1:])

    if start < end and m != start and m != end:
        if l < r:
            return condition_satisfies(a, m, end)
        elif l > r:
            return condition_satisfies(a, 0, m)
        return True
    else:
        return l == r

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print("YES" if condition_satisfies(a, 0, n) else "NO")
