#
# Perform register instructions and find largest values
#

conditions = {">": lambda x, y: x > y,
              "<": lambda x, y: x < y,
              "<=": lambda x, y: x <= y,
              ">=": lambda x, y: x >= y,
              "==": lambda x, y: x == y,
              "!=": lambda x, y: x != y}

def process_instruction(register, instruction):
    instr, cond = instruction.split(' if ')
    cond = cond.split(' ')
    if conditions[cond[1]](register.get(cond[0], 0), int(cond[2])):
        name, operation, value = instr.split(' ')
        value = int(value)
        if not name in register:
            register[name] = 0
        if operation == "inc":
            register[name] += value
        elif operation == "dec":
            register[name] -= value
        return register[name]
    return 0

def find_largest_value(register):
    return max(register.values())

register = {}
largest_value = 0
with open("day08.data", "r") as instructions:
    for instruction in instructions.readlines():
        value = process_instruction(register, instruction)
        if value > largest_value:
            largest_value = value
    
print("Part 1: {}".format(find_largest_value(register)))
print("Part 2: {}".format(largest_value))
