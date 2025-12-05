import sys
from functools import cmp_to_key

data = open(sys.argv[1]).read().strip()
rules_part, updates_part = data.split('\n\n')

rules = set()
for line in rules_part.split('\n'):
    a, b = line.split('|')
    rules.add((int(a), int(b)))

updates = []
for line in updates_part.split('\n'):
    updates.append(list(map(int, line.split(','))))

def is_ordered(update):
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if (update[j], update[i]) in rules:
                return False
    return True

def sort_update(update):
    def cmp(a, b):
        if (a, b) in rules: return -1
        if (b, a) in rules: return 1
        return 0
    return sorted(update, key=cmp_to_key(cmp))

p1 = p2 = 0
for u in updates:
    if is_ordered(u):
        p1 += u[len(u)//2]
    else:
        fixed = sort_update(u)
        p2 += fixed[len(fixed)//2]

print('p1:', p1)
print('p2:', p2)
