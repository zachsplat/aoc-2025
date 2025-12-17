import sys, re

data = open(sys.argv[1]).read()
nums = list(map(int, re.findall(r'\d+', data)))
a, b, c = nums[0], nums[1], nums[2]
program = nums[3:]

def run(a, b, c, program):
    ip = 0
    out = []

    def combo(op):
        if op <= 3: return op
        if op == 4: return a
        if op == 5: return b
        if op == 6: return c
        return 0  # 7 reserved

    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1]

        if opcode == 0:    # adv
            a = a >> combo(operand)
        elif opcode == 1:  # bxl
            b = b ^ operand
        elif opcode == 2:  # bst
            b = combo(operand) % 8
        elif opcode == 3:  # jnz
            if a != 0:
                ip = operand
                continue
        elif opcode == 4:  # bxc
            b = b ^ c
        elif opcode == 5:  # out
            out.append(combo(operand) % 8)
        elif opcode == 6:  # bdv
            b = a >> combo(operand)
        elif opcode == 7:  # cdv
            c = a >> combo(operand)

        ip += 2

    return out

result = run(a, b, c, program)
print('p1:', ','.join(map(str, result)))
# p2 requires finding the right A value, brute force won't work
# need to work backwards from the output
