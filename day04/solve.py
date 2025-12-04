import sys

grid = open(sys.argv[1]).read().strip().split('\n')
rows, cols = len(grid), len(grid[0])

def count_xmas():
    target = "XMAS"
    dirs = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    count = 0
    for r in range(rows):
        for c in range(cols):
            for dr, dc in dirs:
                ok = True
                for i, ch in enumerate(target):
                    nr, nc = r + dr*i, c + dc*i
                    if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != ch:
                        ok = False
                        break
                if ok:
                    count += 1
    return count

def count_x_mas():
    # X shape: two MAS crossing at the A
    count = 0
    for r in range(1, rows-1):
        for c in range(1, cols-1):
            if grid[r][c] != 'A':
                continue
            d1 = grid[r-1][c-1] + grid[r+1][c+1]
            d2 = grid[r-1][c+1] + grid[r+1][c-1]
            if d1 in ('MS', 'SM') and d2 in ('MS', 'SM'):
                count += 1
    return count

print('p1:', count_xmas())
print('p2:', count_x_mas())
