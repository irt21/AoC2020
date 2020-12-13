import numpy as np
import math

def lowest_common_multiple(x, y):
    res = (x * y) / gcd(x, y)
    return res

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

input_filepath = './input.txt'
with open(input_filepath, 'r') as f_in:
    data = f_in.read()

now = int(data.split('\n')[0])
data = data.split('\n')[1]
buses = data.replace(',x', '')
buses = buses.split(',')
print(buses)

# Part one
current_wait = now
for bus in buses:
    bus = int(bus)
    time_since = now % bus
    time_to_wait = bus - time_since
    if time_to_wait < current_wait:
        current_wait = time_to_wait
        current_bus = bus

print("Part one answer=", current_bus*current_wait)

# Part two

times = []
data = data.replace('x', '-1')
times = data.split(',')
times = np.array(times, dtype=np.int32)


times = [17,-1,13,19]
size = len(times)
# print("Times=", times)
print("SIZE=", size)
timestamp = 0
increment = times[0]
idx = 0
while idx < size:
    if times[idx] != -1:
        timestamp = timestamp + increment
        print(idx, "T", timestamp, "I", increment)
        print(timestamp+idx, times[idx])
        if ((timestamp+idx) % (times[idx])) == 0:
            increment = lowest_common_multiple(increment, times[idx])
            idx = idx+1
    else:
        idx = idx+1

print(timestamp)
works = True
for i in range(0, size):
    t_prime = timestamp + i
    if t_prime % times[i] != 0:
        works = False
if works:
    print("HOORAY")
