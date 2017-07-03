def solve(n, p):
    if p > n/2 and n % 2 == 0:
        return (n - p + 1) // 2
    elif p > n/2 and n % 2 != 0:
        return (n - p) // 2
    else:
        return p // 2
    
n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
