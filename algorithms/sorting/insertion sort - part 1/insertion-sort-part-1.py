
def insertion_sort(s, ar):
	v = ar[-1]
	i = s - 2
	
	while i >= 0 and ar[i] > v:
		ar[i+1] = ar[i]
		print(*ar)
		i -= 1
	
	ar[i+1] = v
	print(*ar)

s = int(input())
ar = list(map(int, input().split()))
insertion_sort(s, ar)