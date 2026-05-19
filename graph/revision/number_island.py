grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
island_no = 0



ROWS,COLS = len(grid),len(grid[0])


def dfs(row,col):
    if row < 0 or row >=len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != "1":
        return
    else:
        grid[row][col] = "0"
        dfs(row + 1,col)
        dfs(row - 1,col)
        dfs(row,col+1)
        dfs(row,col-1)


for row in range(ROWS):
    for col in range(COLS):
        if grid[row][col] == "1":
            island_no += 1
            dfs(row,col)

print(island_no)



