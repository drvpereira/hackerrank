import copy

def print_grid(grid):
    for line in grid:
        for c in line:
            print(c, end = '')
        print()
    print()

def try_direction(grid, i, j, word, direction):
    size = 0
    
    if i-direction[0] >= 0 and i-direction[0] < len(grid) and j-direction[1] >= 0 and j-direction[1] < len(grid) and grid[i-direction[0]][j-direction[1]] == '-':
        return False

    while i >= 0 and i < len(grid) and j >= 0 and j < len(grid) and (grid[i][j] == '-' or size < len(word) and word[size] == grid[i][j]):
        size += 1
        i += direction[0]
        j += direction[1]

    return size == len(word)

def write_word(grid, word, i, j, direction):
    for c in word:
        grid[i][j] = c
        i += direction[0]
        j += direction[1]

def erase_word(grid, word, i, j, direction):
    for c in word:
        grid[i][j] = '-'
        i += direction[0]
        j += direction[1]

def try_place_word(grid, words, index, solutions):
    if index >= len(words):
        solutions.append(grid)
        return

    word = words[index]
    new_grid = copy.deepcopy(grid)

    for i in range(len(new_grid)):
        for j in range(len(new_grid)):

            if new_grid[i][j] != '+':

                for direction in [ (-1, 0), (1, 0), (0, -1), (0, 1) ]:

                    if try_direction(new_grid, i, j, word, direction):
                        write_word(new_grid, word, i, j, direction)
                        try_place_word(new_grid, words, index+1, solutions)

                        if len(solutions) == 0:
                            erase_word(new_grid, word, i, j, direction)


grid = []
solutions = []
for _ in range(10):
    grid.append(list(input()))

words = input().split(';')

try_place_word(grid, words, 0, solutions)

for solution in solutions:
    print_grid(solution)