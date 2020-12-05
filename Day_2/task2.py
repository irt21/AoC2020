def correct_index_zero(arr):
    return [x-1 for x in arr]


input_filepath = './input.txt'

mins = []
maxs = []
letters = []
pws = []
with open(input_filepath, 'r') as f_in:
    for line in f_in:
        line = line.split()
        vals = line[0].split('-')
        mins.append(int(vals[0]))
        maxs.append(int(vals[1]))
        letters.append(line[1].rstrip(':'))
        pws .append(line[2])

size = len(mins)
good_sled_pw_count = 0
for i in range(size):
    count = pws[i].count(letters[i])
    if mins[i] <= count <= maxs[i]:
        good_sled_pw_count = good_sled_pw_count + 1

print(good_sled_pw_count)

mins = correct_index_zero(mins)
maxs = correct_index_zero(maxs)

good_toboggan_pw_count = 0
for i in range(size):
    if (pws[i][mins[i]] == letters[i]) ^ (pws[i][maxs[i]] == letters[i]):
        good_toboggan_pw_count = good_toboggan_pw_count + 1
print(good_toboggan_pw_count)
