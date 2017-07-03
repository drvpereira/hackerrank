h = list(map(int, input().strip().split(' ')))
word = input().strip()
heights = [ h[ord(word[i]) - ord('a')] for i in range(len(word)) ]
print(max(heights) * len(word))
