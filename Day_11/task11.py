import numpy as np

def attempt_flip(map, i, j, l_i, l_j):
    if map[i,j] == 0:
        return False
    num_occ = sum_nbours_occ(map, i, j, l_i, l_j)
    if map[i, j] > 0 and num_occ >= 5:
        return True
    elif map[i, j] < 0 and num_occ == 0:
        return True
    else:
        return False

def sum_nbours_occ(grid, i, j, li, lj):
    occ = 0
    for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                search = True
                i_prime = i
                j_prime = j
                while search:
                    i_prime = i_prime + di
                    j_prime = j_prime + dj
                    if j_prime < 0 or j_prime >= lj or i_prime < 0 or i_prime >= li:
                        search = False
                    elif grid[i_prime, j_prime] != 0:
                        search = False
                        if grid[i_prime, j_prime] > 0:
                            occ = occ+1
    if grid[i, j] > 0:
        occ = occ - 1
    return occ

input_filepath = './input.txt'
input = []
with open(input_filepath, 'r') as f_in:
    for line in f_in:
        l = []
        line = line.strip()
        for c in line:
            line = line.strip()
            if c == '.':
                c = 0
            elif c == '#':
                c = 1
            else:
                c = -1
            l.append(c)
        if l:
            input.append(l)

Lj = len(input[0])
Li = len(input)
seats = np.array(input)
print(Li, Lj)
count = 0
change = True
while change:
    new_seats = np.zeros_like(seats)
    change = False
    for i in range(Li):
        for j in range(Lj):
            if attempt_flip(seats, i, j, Li, Lj):
                new_seats[i, j] = -seats[i, j]
                change = True
            else:
                new_seats[i,j] = seats[i,j]
    seats = new_seats
    count = count +1

print(count)
print(np.count_nonzero(seats == 1))
