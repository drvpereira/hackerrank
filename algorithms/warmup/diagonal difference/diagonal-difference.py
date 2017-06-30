n = int(input().strip())
a = [ list(map(int, input().strip().split(' '))) for _ in range(n) ]

totals = [ a[i][i] - a[i][n - i - 1] for i in range(n) ]
    
print(int(abs(sum(totals))))