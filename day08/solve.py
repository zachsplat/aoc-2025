import sys
from itertools import combinations

lines = open(sys.argv[1]).read().strip().split('\n')
rows, cols = len(lines), len(lines[0])

antennas = {}
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch != '.':
            antennas.setdefault(ch, []).append((r, c))

def antinodes_p1():
    nodes = set()
    for freq, positions in antennas.items():
        for (r1,c1), (r2,c2) in combinations(positions, 2):
            dr, dc = r2-r1, c2-c1
            for nr, nc in [(r1-dr, c1-dc), (r2+dr, c2+dc)]:
                if 0 <= nr < rows and 0 <= nc < cols:
                    nodes.add((nr, nc))
    return len(nodes)

def antinodes_p2():
    nodes = set()
    for freq, positions in antennas.items():
        for (r1,c1), (r2,c2) in combinations(positions, 2):
            dr, dc = r2-r1, c2-c1
            # extend in both directions
            r, c = r1, c1
            while 0 <= r < rows and 0 <= c < cols:
                nodes.add((r, c))
                r -= dr; c -= dc
            r, c = r2, c2
            while 0 <= r < rows and 0 <= c < cols:
                nodes.add((r, c))
                r += dr; c += dc
    return len(nodes)

print('p1:', antinodes_p1())
print('p2:', antinodes_p2())
