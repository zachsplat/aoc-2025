import sys, re

data = open(sys.argv[1]).read().strip()
machines = data.split('\n\n')

def solve_machine(ax, ay, bx, by, px, py):
    # solve: ax*a + bx*b = px, ay*a + by*b = py
    det = ax*by - ay*bx
    if det == 0:
        return None
    a = (px*by - py*bx) / det
    b = (ax*py - ay*px) / det
    if a == int(a) and b == int(b) and a >= 0 and b >= 0:
        return int(3*a + b)
    return None

p1 = p2 = 0
for m in machines:
    nums = list(map(int, re.findall(r'\d+', m)))
    ax, ay, bx, by, px, py = nums
    cost = solve_machine(ax, ay, bx, by, px, py)
    if cost is not None:
        p1 += cost
    # p2: add 10000000000000 to prize coords
    cost2 = solve_machine(ax, ay, bx, by, px+10000000000000, py+10000000000000)
    if cost2 is not None:
        p2 += cost2

print('p1:', p1)
print('p2:', p2)
