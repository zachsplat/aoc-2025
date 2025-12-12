import sys
from collections import deque

grid = open(sys.argv[1]).read().strip().split('\n')
rows, cols = len(grid), len(grid[0])
visited = [[False]*cols for _ in range(rows)]

def flood(sr, sc):
    ch = grid[sr][sc]
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    cells = []
    perimeter = 0
    while q:
        r, c = q.popleft()
        cells.append((r, c))
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == ch:
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc))
            else:
                perimeter += 1
    return len(cells), perimeter

total = 0
for r in range(rows):
    for c in range(cols):
        if not visited[r][c]:
            area, perim = flood(r, c)
            total += area * perim
print('p1:', total)
# p2 needs side counting, skipping
