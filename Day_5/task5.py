
def binary_split(start, stop, half):
    rn = stop - start
    half_rn = rn/2
    if half == 'high':
        return start+half_rn, stop
    return start, start+half_rn

def get_seat_id(row, col, N_cols):
    return (row*N_cols) + col

Nrows = 128
Ncols = 8

seat_ids = []

input_filepath = './input.txt'
with open(input_filepath,'r') as f_in:
    for line in f_in:
        line = line.strip()
        r0 = 0
        r = Nrows
        c0 = 0
        c = Ncols
        for L in line:
            if L == 'F':
                r0, r = binary_split(r0, r, 'low')
            elif L == 'B':
                r0, r = binary_split(r0, r, 'high')
            elif L == 'R':
                c0, c = binary_split(c0, c, 'high')
            elif L == 'L':
                c0, c = binary_split(c0, c, 'low')
        seat_ids.append(get_seat_id(r0, c0, Ncols))

seat_ids.sort()
for i in range(len(seat_ids)-1):
    if seat_ids[i] != seat_ids[i+1]-1:
        print(seat_ids[i], seat_ids[i+1])