def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (l[j] > key) and (j >= 0):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key


m = int(input().strip())
ar = list(map(int, input().strip().split()))
insertion_sort(ar)
print(*ar)
