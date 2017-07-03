
def bubble_sort(ar):
	swaps = 0

	for i in range(len(ar)):
		for j in range(i, len(ar)):
			if ar[i] > ar[j]:
				temp = ar[i]
				ar[i] = ar[j]
				ar[j] = temp
				swaps += 1
	return swaps

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))

swaps = bubble_sort(ar)

print("Array is sorted in " + str(swaps) + " swaps.")
print("First Element: " + str(ar[0]))
print("Last Element: " + str(ar[-1]))