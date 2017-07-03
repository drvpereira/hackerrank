
def hourglass(arr, i, j):
   return arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

arr = [ [ int(i) for i in input().strip().split() ] for _ in range(6) ]

max_h = float('-Inf')
for i in range(4):
    for j in range(4):
        max_h = max(max_h, hourglass(arr, i, j))

print(max_h)