from math import floor, sqrt

def is_between(n, a, b):
    return all(n % i == 0 for i in a) and all(i % n == 0 for i in b)

n, m = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))

min_val = min(min(a), min(b))
max_val = max(max(a), max(b))
numbers = []

for i in range(min_val, max_val+1):
    if is_between(i, a, b):
        numbers.append(i)
        
print(len(numbers))