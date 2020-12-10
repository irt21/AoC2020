import numpy as np

def populate_preamble(length, inputs):
    pmble = inputs[:length]
    return pmble


def populate_matrix(nums):
    matrix = np.add.outer(nums, nums)
    return matrix


def check_any_matrix(matrix, key):
    if (matrix == key).any():
        return True
    return False


def check_contiguous_sum(nums, key, crawl):
    for s in range(len(nums)- crawl):
        val = sum(nums[s:s+crawl])
        if val == key:
            return nums[s:s+crawl]
    return []


def update_preamble(pmble, new_entry):
    pmble.pop(0)
    pmble.append(new_entry)
    return pmble


input_filepath = './input.txt'
input = []
with open(input_filepath, 'r') as f_in:
    for line in f_in:
        line = line.strip()
        input.append(int(line))

SIZE = 25
numbers = populate_preamble(SIZE, input)
found = True

for i in input[SIZE:]:
    sums = populate_matrix(numbers)
    found = check_any_matrix(sums, i)
    if not found:
        print(i)
        weakness = i
        break
    numbers = update_preamble(numbers, i)

sums = populate_matrix(input)
for i in range(2, len(input)):
    values = check_contiguous_sum(input, weakness, i)
    if values:
        print(values)
        print(min(values) + max(values))