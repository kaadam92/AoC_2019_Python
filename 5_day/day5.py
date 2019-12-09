def intcode_addition(op1, op2):
    return op1 + op2


def intcode_multiplication(op1, op2):
    return op1 * op2


def intcode_output(addr):
    return addr


def intcode_input(addr):
    return addr


def intcode_machine(opcodes):
    finished = 0
    pc = 0

    while finished == 0: # Addition
        if opcodes[pc] == 1:
            opcodes[opcodes[pc + 3]] = opcodes[opcodes[pc + 1]] + opcodes[opcodes[pc + 2]]
            opcodes[opcodes[pc + 3]] = intcode_addition(opcodes[opcodes[pc + 1]],opcodes[opcodes[pc + 2]])
            pc += 4
        elif opcodes[pc] == 2: # Multiplication
            op_1 = opcodes[opcodes[pc + 1]]
            op_2 = opcodes[opcodes[pc + 2]]
            pos = opcodes[pc + 3]
            opcodes[pos] = op_1 * op_2
            pc += 4
        elif opcodes[pc] == 3: # Input
            pass
        elif opcodes[pc] == 4: # Output
            pass
        elif opcodes[pc] == 99:
            finished = 1
            print("END!")
            break
        else:
            pass

    return opcodes[0]


print("AoC 2019 Day 5 - Python")
print('-------------PART I------------')

debug = 1

f = open("data.txt", "r")
opcodes = f.read().split(',')


for x in opcodes:
    if debug == 1:
        print("Opcode: {}".format(x))
    opcodes[opcodes.index(x)] = (int)(x)

opcode_length = len(opcodes)
opcode_cnt = 0
finished = 0
i = 0

opcodes_orig = opcodes.copy()

opcodes[1] = 12
opcodes[2] = 2

intcode_machine(opcodes)

print("Opcode: {}".format(opcodes[0]))

print('-------------PART II------------')

opcodes = opcodes_orig.copy()

noun = 0
verb = 0
pair_found = 0

desired_resoult = 19690720

for noun_test in range(100):

    for verb_test in range(100):
        if debug == 1:
            print("Testing with noun: {} verb: {}".format(noun_test, verb_test))
        opcodes[1] = noun_test
        opcodes[2] = verb_test
        if desired_resoult == intcode_machine(opcodes):
            pair_found = 1
            noun = noun_test
            verb = verb_test
            break
        opcodes = opcodes_orig.copy()
    if pair_found == 1:
        break


print("Noun: {}".format(noun))
print("Verb: {}".format(verb))

result = 100 * noun + verb
print("Result: {}".format(result))




print("Data read complete.")
