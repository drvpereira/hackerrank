n = int(input())
candies_left = [ 1 for _ in range(n) ]
candies_right = [ 1 for _ in range(n) ]
ratings = [ int(input()) for _ in range(n) ]
previous_left, previous_right = ratings[0], ratings[n-1]

for i in range(n):
    current_left = ratings[i]
    current_right = ratings[n - i - 1]
    
    if current_left > previous_left:
        candies_left[i] = candies_left[i-1] + 1
    if current_right > previous_right:
        candies_right[n - i - 1] = candies_right[n - i] + 1        
        
    previous_left = current_left
    previous_right = current_right
    
print(sum(max(candies_left[i], candies_right[i]) for i in range(n)))