def parse_list_sets(lst):
    sets = [set(l) for l in lst]
    true_set = sets[0]
    for s in sets[1:]:
        true_set = true_set & s
    return true_set


def parse_set(data):
    ans = set(data)
    return ans


input_filepath = './input.txt'
answers = []
with open(input_filepath, 'r') as f_in:
    group_data = []
    for line in f_in:
        line = line.strip()
        if line:
            group_data.append(line)
        else:
            answers.append(parse_list_sets(group_data))
            group_data = []
if group_data:
    answers.append(parse_list_sets(group_data))

print(sum([len(s) for s in answers]))