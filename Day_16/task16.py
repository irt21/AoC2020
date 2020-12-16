import numpy as np

def check_ticket(tick, roolz):
    invalid_fields = []
    for field in tick:
        valid = False
        for key in roolz:
            for ran in roolz[key]:
                if field in ran:
                    valid = True
        if not valid:
            invalid_fields.append(field)
    return invalid_fields

def validate_positions(rools, field_entries, num_fields):
    correlation = np.ones((num_fields, num_fields))
    fields_left = list(range(num_fields))
    keys_left = list(range(num_fields))
    keys = list(rools.keys())
    for f_idx in fields_left:
        for k_idx in keys_left:
            key = keys[k_idx]
            possible = check_all_tickets(field_entries[f_idx, :], rools[key])
            if not possible:
                correlation[f_idx, k_idx] = 0

    while len(keys_left) > 0:
        for f_idx in fields_left:
            if np.sum(correlation[f_idx, :]) == 1:
                k = np.where(correlation[f_idx, :] == 1)[0][0]
                correlation[:, k] = 0
                correlation[f_idx, k] = 1
                fields_left.remove(f_idx)
                keys_left.remove(k)
    result = condense_matrix(correlation, keys, num_fields)
    return result

def check_all_tickets(all_entries, rule):

    res = None
    for r in rule:
        start = r.start
        stop = r.stop
        test = np.logical_and(all_entries >= start, all_entries < stop)
        res = np.logical_or(res, test)
    res = np.all(res)
    return res

def condense_matrix(matrix, cols, N_rows):
    res = {}
    for r in np.arange(N_rows):
        idx = np.where(matrix[r, :] == 1)[0][0]
        res[cols[idx]] = r
    return res


range_rules = {}
rules_filepath = './rules.txt'
with open(rules_filepath, 'r') as f_in:
    for line in f_in:
        line = line.split(': ')
        name = line[0]
        range_rules[name] = []
        rans = line[1].strip().split(' or ')
        for r in rans:
            start, end = r.split('-')
            range_rules[name].append(range(int(start), int(end) + 1))

tickets = []
tickets_filepath = './tickets.txt'
with open(tickets_filepath, 'r') as f_in:
    for line in f_in:
        line = line.split(',')
        for i in range(len(line)):
            line[i] = int(line[i])
        tickets.append(line)
my_ticket = tickets[0]
del(tickets[0])

# Part One
error_rate = 0
for t in tickets:
    bad_fields = check_ticket(t, range_rules)
    for b in bad_fields:
        error_rate = error_rate + b

print(error_rate)

# Part Two
valid_tickets = []
for t in tickets:
    if len(check_ticket(t, range_rules)) == 0:
        valid_tickets.append(t)

num_fields = len(valid_tickets[0])
num_ticks = len(valid_tickets)
field_entries = np.zeros((num_fields, num_ticks))

for f in range(num_fields):
    for t in range(num_ticks):
        field_entries[f, t] = valid_tickets[t][f]

name_to_loc = validate_positions(range_rules, field_entries, num_fields)
answer = 1
for name in name_to_loc:
    if name.startswith('departure'):
        field = name_to_loc[name]
        answer = answer* my_ticket[field]
print(answer)
