
def insertion_sort(ar):
	for i in range(1, len(ar)):
		j = i-1
		v = ar[i]

		while j >= 0 and ar[j] > v:
			ar[j+1] = ar[j]
			j -= 1
		ar[j+1] = v
			
		print(*ar)

s = int(input())
ar = list(map(int, input().split()))
insertion_sort(ar)

