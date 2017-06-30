for _ in range(int(input())):
    n,c,m = map(int, input().split())

    b = n // c
    e = b // m     
    r = b % m
    
    while e > 0:        
        b += e
        r += e % m
        e //= m
    
    print(b + r // m)
    