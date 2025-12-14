import sys, re

lines = open(sys.argv[1]).read().strip().split('\n')
W, H = 101, 103

robots = []
for line in lines:
    px, py, vx, vy = map(int, re.findall(r'-?\d+', line))
    robots.append((px, py, vx, vy))

def simulate(steps):
    positions = []
    for px, py, vx, vy in robots:
        x = (px + vx * steps) % W
        y = (py + vy * steps) % H
        positions.append((x, y))
    return positions

def quadrant_score(positions):
    mx, my = W // 2, H // 2
    q = [0, 0, 0, 0]
    for x, y in positions:
        if x == mx or y == my:
            continue
        qi = (0 if x < mx else 1) + (0 if y < my else 2)
        q[qi] += 1
    return q[0] * q[1] * q[2] * q[3]

print('p1:', quadrant_score(simulate(100)))
# p2: find the christmas tree frame (minimum variance or something)
# too lazy to implement visualization, just checked manually
