def get_outers(roolz):
    inverse_roolz = {}
    for k in roolz:
        arr = []
        for k_prime in roolz:
            if k in roolz[k_prime]:
                arr.append(k_prime)
        inverse_roolz[k] = arr
    return inverse_roolz


def exhaust_search(root, mapping, known):
    for x in mapping[root]:
        if x not in known:
            known.append(x)
            known = exhaust_search(x, mapping, known)
    return known


def sum_search(root, map_vals, map_counts):
    # Total is the weight of the root node in the tree, ie the sum of all nodes below it
    total = 0
    keys = map_vals[root]
    for i in range(len(keys)):
        x = keys[i]
        c = map_counts[root][i]
        if x != 'other':
            contents = sum_search(x, map_vals, map_counts)
            total = total + (c * contents)
        else:
            return 1
    # Add plus 1 for the bag (node) itself
    return total + 1


input_filepath = './input.txt'
rules = {}
counts = {}
with open(input_filepath, 'r') as f_in:
    for line in f_in:
        line = line.strip().rstrip('.')
        line = line.replace(' bags', '')
        line = line.replace(' bag', '')
        line = line.split(' contain ')
        outer = line[0]
        inners = line[1].split(', ')
        nums = []
        for idx in range(len(inners)):
            lst = inners[idx].split(' ')
            inner = ' '.join(lst[1:])
            if inner == 'other':
                nums.append(1)
            else:
                nums.append(int(lst[0]))
            inners[idx] = inner
        rules[outer] = inners
        counts[outer] = nums


inverse_rules = get_outers(rules)
print(len(exhaust_search('shiny gold', inverse_rules, [])))

lst = sum_search('shiny gold', rules, counts)
# Sub one off for the root bag itself
print(lst-1)
