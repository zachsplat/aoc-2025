import sys

def is_safe(nums):
    diffs = [b - a for a, b in zip(nums, nums[1:])]
    if all(1 <= d <= 3 for d in diffs):
        return True
    if all(-3 <= d <= -1 for d in diffs):
        return True
    return False

def is_safe_dampened(nums):
    if is_safe(nums):
        return True
    # try removing each one
    for i in range(len(nums)):
        sub = nums[:i] + nums[i+1:]
        if is_safe(sub):
            return True
    return False

lines = open(sys.argv[1]).read().strip().split('\n')
reports = [list(map(int, l.split())) for l in lines]
print('p1:', sum(1 for r in reports if is_safe(r)))
print('p2:', sum(1 for r in reports if is_safe_dampened(r)))
