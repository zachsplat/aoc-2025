import sys

def part1(lines):
    left, right = [], []
    for line in lines:
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))
    left.sort()
    right.sort()
    return sum(abs(a - b) for a, b in zip(left, right))

def part2(lines):
    left, right = [], []
    for line in lines:
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))
    from collections import Counter
    rc = Counter(right)
    return sum(n * rc[n] for n in left)

lines = open(sys.argv[1]).read().strip().split('\n')
print('p1:', part1(lines))
print('p2:', part2(lines))
