
n = int(input().strip())
scores = sorted(set(map(int, input().strip().split(' '))), reverse = True)
m = int(input().strip())
alice = list(map(int, input().strip().split(' ')))

current_index = len(scores)
previous_score = float('inf')

for i in range(m):
    alice_score = alice[i]
    
    for j in reversed(range(current_index)):
        if scores[j] <= alice_score:
            current_index = j
            previous_score = scores[j]
        else:
            break
            
    print(current_index + 1)