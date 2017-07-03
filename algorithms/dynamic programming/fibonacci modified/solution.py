t1, t2, n = map(int, input().strip().split(' '))
fib = [t1, t2]

for i in range(2, n):
    fib.append((fib[i - 1])*(fib[i - 1]) + fib[i-2])

print(fib[-1])