import sys
from itertools import product

lines = open(sys.argv[1]).read().strip().split('\n')

def can_make(target, nums, ops):
    for combo in product(ops, repeat=len(nums)-1):
        val = nums[0]
        for i, op in enumerate(combo):
            if op == '+':
                val += nums[i+1]
            elif op == '*':
                val *= nums[i+1]
            elif op == '||':
                val = int(str(val) + str(nums[i+1]))
        if val == target:
            return True
    return False

p1 = p2 = 0
for line in lines:
    target, rest = line.split(': ')
    target = int(target)
    nums = list(map(int, rest.split()))
    if can_make(target, nums, ['+', '*']):
        p1 += target
    if can_make(target, nums, ['+', '*', '||']):
        p2 += target

print('p1:', p1)
print('p2:', p2)
