grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

is_lands = 0

ROWS,COLS = len(grid),len(grid[0])

def dfs(row,col):
    if row >= ROWS or row < 0 or col >= COLS or col < 0 or grid[row][col] != "1":
        return

    grid[row][col] = "0"
    dfs(row + 1,col)
    dfs(row - 1,col)
    dfs(row,col + 1)
    dfs(row,col - 1)


for row in range(ROWS):
    for col in range(COLS):
        if grid[row][col] == "1":
            is_lands +=1
            dfs(row,col)


print(is_lands)