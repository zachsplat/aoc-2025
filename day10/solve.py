import sys
from collections import deque

grid = []
for line in open(sys.argv[1]).read().strip().split('\n'):
    grid.append([int(c) for c in line])
rows, cols = len(grid), len(grid[0])

def trailhead_score(sr, sc):
    """bfs from 0, count reachable 9s"""
    visited = set()
    q = deque([(sr, sc)])
    visited.add((sr, sc))
    nines = set()
    while q:
        r, c = q.popleft()
        if grid[r][c] == 9:
            nines.add((r, c))
            continue
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited:
                if grid[nr][nc] == grid[r][c] + 1:
                    visited.add((nr, nc))
                    q.append((nr, nc))
    return len(nines)

def trailhead_rating(sr, sc):
    """count distinct paths from 0 to any 9"""
    # dfs with path counting
    count = [0]
    def dfs(r, c):
        if grid[r][c] == 9:
            count[0] += 1
            return
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == grid[r][c] + 1:
                    dfs(nr, nc)
    dfs(sr, sc)
    return count[0]

p1 = p2 = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 0:
            p1 += trailhead_score(r, c)
            p2 += trailhead_rating(r, c)
print('p1:', p1)
print('p2:', p2)
