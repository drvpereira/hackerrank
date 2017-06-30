
def palindrome_index(s):
    left = 0
    right = len(s) - 1
    palindrome = True

    while left < right:
    	if s[left] == s[right]:
    		left += 1
    		right -= 1
    	else:
    		palindrome = False
    		break

    if palindrome:
    	return -1

    left_pointer, right_pointer = left, right-1
    
    while left_pointer < right_pointer and s[left_pointer] == s[right_pointer]:
    	left_pointer += 1
    	right_pointer -= 1

    if left_pointer == right_pointer or left_pointer == right_pointer + 1:
    	return right
    else:
    	return left


for _ in range(int(input())):
	s = input()
	print(palindrome_index(s))
