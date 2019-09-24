from heart_grid import grid


counter = 0
x = 0

for counter in range(len(grid[x])):
    for x in range(len(grid)):
        print(grid[x][counter], end='')

    print()
