import numpy as np

def valid_connection(j1, j2):
    diff = j2 - j1
    if 0 < diff <= 3:
        return True
    return False

def extend_chain(chain, avail, candidates):
    if len(candidates) == 1:
        return candidates
    for a_idx in range(len(avail)):
        if valid_connection(chain[-1], avail[a_idx]):
            new_chain = chain + [avail[a_idx]]
            new_avail = avail.copy()
            del (new_avail[a_idx])
            # print(len(chain), len(new_chain), len(avail), len(new_avail))
            candidates = extend_chain(new_chain, new_avail, candidates)
            if len(candidates) == 1:
                break
    # If there are no valid options left
    if len(avail) == 0:
        candidates.append(chain)
    return candidates

def get_diffs(arr):
    diffs = []
    for i in range(1, len(arr)):
        diffs.append(arr[i] - arr[i-1])
    return diffs


input_filepath = './input.txt'
input = []
with open(input_filepath, 'r') as f_in:
    for line in f_in:
        line = line.strip()
        input.append(int(line))

input.sort()
device_input = input[-1] +3
print(device_input)
input.append(device_input)

res = extend_chain([0], input, [])
res = res[0]
print(len(res), len(input))
print(res[-1])
jolt_diffs = get_diffs(res)
print(jolt_diffs.count(1)*jolt_diffs.count(3))

# Add the 0 jolt adapter to the start of our chain, before we passed [0] in as the root
input.insert(0,0)
print(input)
num_paths = []
for i in input:
    num_paths.append(0)
# Intialise the 0 jolt adapter to only have one path
num_paths[0] = 1
for i in range(1, len(num_paths)):
    jolts = input[i]
    for j in range(len(num_paths)):
        prev = input[j]
        if 0 < (jolts - prev) <= 3:
            num_paths[i] = num_paths[i] + num_paths[j]

print(num_paths)
print(num_paths[-1])

