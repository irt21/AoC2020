def run_sequence(commands, arguments):
    visited = []
    index = 0
    accumulator = 0
    success = True
    while index < len(cmd):
        visited.append(index)
        new_index, accumulator = do_cmd(commands[index], arguments[index], index, accumulator)
        if new_index in visited:
            success = False
            break
        index = new_index
    return accumulator, success

def do_cmd(command, argument, idx, acc_val):
    if command == 'acc':
        acc_val = acc_val+argument
        idx = idx+1
    elif command == 'jmp':
        idx = idx+argument
    else: # The nop
        idx = idx+1
    return idx, acc_val

input_filepath = './input.txt'
cmd = []
args = []
with open(input_filepath, 'r') as f_in:
    for line in f_in:
        line = line.strip().split(' ')
        cmd.append(line[0])
        args.append(int(line[1]))

accumulator_value, _ = run_sequence(cmd, args)

print(accumulator_value)

for idx in range(len(cmd)):
    if cmd[idx] == 'nop':
        orig = 'nop'
        cmd[idx] = 'jmp'
    elif cmd[idx] == 'jmp':
        orig = 'jmp'
        cmd[idx] = 'nop'
    else:
        continue
    accumulator_value, correct = run_sequence(cmd, args)
    if correct:
        print(accumulator_value)
        break
    else:
        cmd[idx] = orig
