import sys

data = open(sys.argv[1]).read()
grid_part, moves_part = data.split('\n\n')
grid = [list(row) for row in grid_part.strip().split('\n')]
moves = moves_part.replace('\n', '')

rows, cols = len(grid), len(grid[0])

# find robot
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '@':
            robot = (r, c)
            grid[r][c] = '.'
            break

DIRS = {'^': (-1,0), 'v': (1,0), '<': (0,-1), '>': (0,1)}

r, c = robot
for move in moves:
    if move not in DIRS:
        continue
    dr, dc = DIRS[move]
    nr, nc = r + dr, c + dc
    if grid[nr][nc] == '.':
        r, c = nr, nc
    elif grid[nr][nc] == 'O':
        # push chain of boxes
        er, ec = nr, nc
        while grid[er][ec] == 'O':
            er += dr
            ec += dc
        if grid[er][ec] == '.':
            grid[er][ec] = 'O'
            grid[nr][nc] = '.'
            r, c = nr, nc

gps = 0
for rr in range(rows):
    for cc in range(cols):
        if grid[rr][cc] == 'O':
            gps += 100 * rr + cc
print('p1:', gps)
