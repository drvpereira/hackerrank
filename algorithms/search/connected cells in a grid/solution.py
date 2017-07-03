
def mark_region(grid, i, j, regions, region_number):
	grid[i][j] = chr(region_number)

	for x in [-1, 0, 1]:
		for y in [-1, 0, 1]:
			if i+x >= 0 and i+x < len(grid) and j+y >= 0 and j+y < len(grid[0]) and grid[i+x][y+j] == 1:
				regions[region_number] += 1
				mark_region(grid, i+x, j+y, regions, region_number)



def find_region(grid, n, m):
	region_number = ord('A')
	regions = {}

	for i in range(n):
		for j in range(m):
			if grid[i][j] == 1:
				regions[region_number] = 1
				mark_region(grid, i, j, regions, region_number)
				region_number += 1

	return regions

n, m = int(input()), int(input())
grid = []

for _ in range(n):
	grid.append(list(map(int, input().split())))

regions = find_region(grid, n, m)

print(max(regions.values()))