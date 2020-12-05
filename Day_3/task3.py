def check_slope(mp, dx, dy, lx, ly):
    pos_x = 0
    count = 0
    for pos_y in range(0, ly, dy):
        if mp[pos_y][pos_x] == tree:
            count = count + 1
        pos_x = (pos_x + dx) % lx
    return count


input_filepath = './input.txt'
space = '.'
tree = '#'
slope_map = []
with open(input_filepath, 'r') as f_in:
    for line in f_in:
        line = line.strip()
        line = list(line)
        slope_map.append(line)

len_x = len(slope_map[0])
len_y = len(slope_map)
diff_x = [1, 3, 5, 7, 1]
diff_y = [1, 1, 1, 1, 2]

res = 1
for i in range(len(diff_y)):
    tree_count = check_slope(slope_map, diff_x[i], diff_y[i], len_x, len_y)
    res = res*tree_count
print(res)
