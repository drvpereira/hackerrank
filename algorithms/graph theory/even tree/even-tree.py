
def count_children(n, tree):
	count = len(tree[n])
	for c in tree[n]:
		count += count_children(c, tree)
	return count

def remove_child(c, tree):
	removed = False
	for n in tree:
		if c in tree[n]:
			tree[n].remove(c)
			removed = True
			break
	return removed

n, e = map(int, input().split())

tree = { i+1:[] for i in range(n) }
for _ in range(e):
	n1, n2 = map(int, input().split())
	tree[n2].append(n1)

edges = 0
removed = True
while removed:
	for n in tree:
		children_no = 1 + count_children(n, tree)
		if children_no % 2 == 0:
			if remove_child(n, tree):
				edges += 1
				removed = True
	removed = False

print(edges)