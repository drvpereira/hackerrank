input()
ar = list(map(int, input().split()))
l = [ i for i in ar if i < ar[0] ] + [ ar[0] ] + [ i for i in ar if i > ar[0] ]
print(*l)