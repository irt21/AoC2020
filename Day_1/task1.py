import numpy as np


def calculate_product_of_sum_terms(sum_arr, arr, sum_val):
    indices = np.where(sum_arr == sum_val)
    indices = [i[0] for i in indices]
    res = 1
    for i in indices:
        res = res * arr[i]
    return res


inputs = []
input_path = './input.txt'
with open(input_path, 'r') as f_in:
    for line in f_in:
        x = line.strip()
        inputs.append(int(x))

target = 2020

inputs = np.array(inputs)

twoD_grid = np.add.outer(inputs, inputs)
threeD_grid = np.add.outer(twoD_grid, inputs)

print(calculate_product_of_sum_terms(twoD_grid, inputs, target))
print(calculate_product_of_sum_terms(threeD_grid, inputs, target))
