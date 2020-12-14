import math


def apply_mask(x_int, mask):
    x_bin = list(format(x_int, 'b').rjust(36, '0'))
    for i in range(len(x_bin)):
        #print(i, type(i))
        if mask[i] != 'X':
            x_bin[i] = mask[i]
    x_bin = ''.join(x_bin)
    #print(x_bin)
    return int(x_bin, 2)

def apply_mutant_mask(x_int, mask):
    x_bin = list(format(x_int, 'b').rjust(36, '0'))
    addresses = []
    num_x = mask.count('X')
    mutations = math.pow(2, num_x)
    for m in range(int(mutations)):
        new_address = []
        mutant = list(format(m, 'b').rjust(num_x, '0'))
        m_count = num_x - 1
        for i in range(len(x_bin)):
            if mask[i] == '1':
                new_address.append('1')
            elif mask[i] == '0':
                new_address.append(x_bin[i])
            elif mask[i] == 'X':
                new_address.append(mutant[m_count])
                m_count = m_count - 1
        new_address = ''.join(new_address)
        addresses.append(int(new_address, 2))
    return addresses


# PART 1
memory = {}

input_filepath = './input.txt'
with open(input_filepath, 'r') as f_in:
    for line in f_in:
        if line.startswith('mask'):
            current_mask = line.split(' = ')[1].strip()
            # print(current_mask, type(current_mask))
        else:
            mem = line[line.index('[')+1:line.index(']')]
            mem = int(mem)
            value = line.split(' = ')[1].strip()
            value = int(value)

            store = apply_mask(value, current_mask)
            # print("Storing", store, "in", mem)
            memory[mem] = store

sum = 0
for val in memory.values():
    sum = sum + val

print("SUM=", sum)

# PART 2
memory = {}

input_filepath = './input.txt'
with open(input_filepath, 'r') as f_in:
    for line in f_in:
        if line.startswith('mask'):
            current_mask = line.split(' = ')[1].strip()
            # print(current_mask, type(current_mask))
        else:
            mem = line[line.index('[')+1:line.index(']')]
            mem = int(mem)
            value = line.split(' = ')[1].strip()
            value = int(value)

            mems = apply_mutant_mask(mem, current_mask)
            for m in mems:
                # print("Storing", store, "in", mem)
                memory[m] = value

sum = 0
for val in memory.values():
    sum = sum + val

print("SUM=", sum)