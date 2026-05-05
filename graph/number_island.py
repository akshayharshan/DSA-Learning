grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

def dfs(row,col):
    if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != "1":
        return
    else:
        grid[row][col] = "0"
        dfs(row,col+1)
        dfs(row,col-1)
        dfs(row-1,col)
        dfs(row+1,col)
rows,cols = len(grid),len(grid[0])
island_count = 0
for row in range(rows):
    for col in range(cols):
        if grid[row][col] == "1":
            island_count+=1
            dfs(row,col)
print(island_count)