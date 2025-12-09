import sys

disk_map = open(sys.argv[1]).read().strip()

def expand(dm):
    blocks = []
    file_id = 0
    is_file = True
    for ch in dm:
        n = int(ch)
        if is_file:
            blocks.extend([file_id] * n)
            file_id += 1
        else:
            blocks.extend([-1] * n)
        is_file = not is_file
    return blocks

def compact_p1(blocks):
    b = list(blocks)
    l, r = 0, len(b) - 1
    while l < r:
        if b[l] != -1:
            l += 1
        elif b[r] == -1:
            r -= 1
        else:
            b[l], b[r] = b[r], b[l]
            l += 1
            r -= 1
    return b

def checksum(blocks):
    return sum(i * b for i, b in enumerate(blocks) if b >= 0)

blocks = expand(disk_map)
print('p1:', checksum(compact_p1(blocks)))
# p2 is whole-file compaction, skipping for now it's annoying
