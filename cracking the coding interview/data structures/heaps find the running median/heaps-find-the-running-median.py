
def median(array):
	if len(array) > 0:
		middle = len(array) // 2

		if len(array) % 2 == 0:
			return (array[middle - 1] + array[middle]) / 2
		else:
			return array[middle]
	else:
		return 0

def bsinsert(array, value):
	if len(array) == 0:
		array.append(value)
		return

	lb = 0
	rb = len(array) - 1

	while lb < rb:
		middle = (lb + rb)  // 2

		if array[middle] > value:
			rb = middle - 1
		else:
			lb = middle + 1

	if array[lb] > value:
		array.insert(lb, value)
	else:
		array.insert(lb+1, value)

result = []    
for _ in range(int(input())):
   value = int(input())
   bsinsert(result, value)
   print("%.1f" % median(result))