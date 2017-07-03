def fibo(n):
	n1 = 1
	n2 = 0

	if n > 1:
		for i in range(n-2):
			n1 = n1 + n2
			n2 = n1 - n2

	return(n1+n2)

n = int(input())
print(fibo(n))