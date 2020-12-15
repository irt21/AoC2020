def play_game_dict(spoken_memory, turns, start_num, start_idx):
    next = start_num
    for idx in range(start_idx, turns):
        last = next
        next = turn(spoken_memory, last, idx)
        #last_spoken[next] = idx
        spoken_memory = update_recents(spoken_memory, next, idx)
    return spoken_memory


def turn(memory, recent, turn_num):
    if recent in memory and len(memory[recent]) == 2:
        x = memory[recent][1] - memory[recent][0]
    elif recent in memory:
        x = 0
    else:
        x = 0
    return x

def update_recents(mapping, spoken, turn):
    if spoken in mapping and len(mapping[spoken]) == 2:
        mapping[spoken][0] = mapping[spoken][1]
        mapping[spoken][1] = turn
    elif spoken in mapping:
        mapping[spoken].append(turn)
    else:
        mapping[spoken] = [turn]
    return mapping

def find_in_memory(mem, val):
    for key, value in mem.items():
        if val in value:
            return key

# PART 1
game_memory = {}

input_filepath = './input.txt'
with open(input_filepath, 'r') as f_in:
    data = f_in.read()
    seq = data.split(',')
    for s in range(len(seq)):
        game_memory[int(seq[s])] = [int(s)]

# Part one
target = 2020 - 1
seq = np.array(seq, dtype=int)
prefix = len(seq)
game_memory = play_game_dict(game_memory, target+1, seq[-1], prefix)
print(find_in_memory(game_memory, target))

# Part two
game_memory = {}
for s in range(len(seq)):
    game_memory[int(seq[s])] = [int(s)]
target = 30000000 - 1
game_memory = play_game_dict(game_memory, target+1, seq[-1], prefix)
print(find_in_memory(game_memory, target))
