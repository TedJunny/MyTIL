# It's about Dynamic Programming
def min_path_sum(grid):
    cols = len(grid[0])
    rows = len(grid)
    new_grid = [[0 for col in range(cols)] for row in range(rows)]

    for i in range(cols):
        if i == 0:
            new_grid[0][0] = grid[0][0]
            continue
        new_grid[0][i] = new_grid[0][i - 1] + grid[0][i]

    for i in range(rows):
        if i == 0:
            continue
        new_grid[i][0] = new_grid[i - 1][0] + grid[i][0]

    for i in range(1, rows):
        for j in range(1, cols):
            if new_grid[i - 1][j] <= new_grid[i][j - 1]:
                new_grid[i][j] = grid[i][j] + new_grid[i - 1][j]
            else:
                new_grid[i][j] = grid[i][j] + new_grid[i][j - 1]

    return new_grid[rows - 1][cols - 1]


min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
