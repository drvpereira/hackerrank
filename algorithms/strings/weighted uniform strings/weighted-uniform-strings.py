
weight_a = ord('a') - 1

def all_uniform_substrings(s):
	weights = set()
	current_char = ''
	current_weight = 0
    
	for i in range(len(s)):
		if current_char != s[i]:
			current_char = s[i]
			current_weight = ord(s[i]) - weight_a
		else:
			current_weight += ord(s[i]) - weight_a
		
		weights.add(current_weight)

	return weights

s = input().strip()
weights = all_uniform_substrings(s)
for _ in range(int(input())):
	print('Yes' if int(input()) in weights else 'No')