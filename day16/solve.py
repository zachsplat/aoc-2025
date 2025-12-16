import sys
import heapq

grid = open(sys.argv[1]).read().strip().split('\n')
rows, cols = len(grid), len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'S': start = (r, c)
        if grid[r][c] == 'E': end = (r, c)

# dijkstra with direction state
# directions: 0=east, 1=south, 2=west, 3=north
DR = [0, 1, 0, -1]
DC = [1, 0, -1, 0]

INF = float('inf')
dist = {}
pq = [(0, start[0], start[1], 0)]  # cost, r, c, dir (facing east)
dist[(start[0], start[1], 0)] = 0

while pq:
    cost, r, c, d = heapq.heappop(pq)
    if cost > dist.get((r, c, d), INF):
        continue

    # move forward
    nr, nc = r + DR[d], c + DC[d]
    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
        nc_cost = cost + 1
        if nc_cost < dist.get((nr, nc, d), INF):
            dist[(nr, nc, d)] = nc_cost
            heapq.heappush(pq, (nc_cost, nr, nc, d))

    # turn left/right
    for nd in [(d + 1) % 4, (d + 3) % 4]:
        tc = cost + 1000
        if tc < dist.get((r, c, nd), INF):
            dist[(r, c, nd)] = tc
            heapq.heappush(pq, (tc, r, c, nd))

best = min(dist.get((end[0], end[1], d), INF) for d in range(4))
print('p1:', best)
