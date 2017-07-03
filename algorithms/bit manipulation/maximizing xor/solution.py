l, r = int(input()), int(input())
print(max([ i^j for i in range(l,r+1) for j in range(i,r+1)]))
