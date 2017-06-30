
def partition(ar):
	if len(ar) > 1:
		l = partition([ i for i in ar if i < ar[0] ]) + [ ar[0] ] + partition([ i for i in ar if i > ar[0] ])
		print(*l)
		return l
	else:
		return ar

input()
partition(list(map(int, input().split())))