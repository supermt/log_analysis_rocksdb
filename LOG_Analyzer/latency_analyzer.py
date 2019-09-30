#!/usr/bin/python3

import matplotlib.pyplot as plt
import matplotlib.animation as animation

import numpy as np
import random


def Average(lst):
    return round(sum(lst)/len(lst), 2)



data = open('run_log_large.txt', 'r')
line = data.readline()
max_key = 0
min_key = 0xffffffffffffffff

values = []
x = 0

couting = {}
latencies = {}
while line:

    if line.split(',')[0] == "Point":
        value = line.split(',')[1]  # Delimiter is comma
        latency = int(line.split(',')[2].replace("\n", ""))
        value = int(value.replace("user", ""))
        if value > max_key:
            max_key = value
        if value < min_key:
            min_key = value
        couting[value] = couting.get(value, 0) + 1
        # latencies[value] = latencies.get(value,[]).append(latency)
        latencies[value] = latencies.get(value, [])
        latencies[value].append(latency)
    line = data.readline()

x_r = []
y_r = []

avg_latency = []
max_latency = []
min_latency = []

temp = 0.0
for key, value in sorted(couting.items(), key=lambda item: item[1]):
    # temp += couting[key]
    x_r.append(key)
    y_r.append(value)
    avg_latency.append(Average(latencies[key]))
    max_latency.append(max(latencies[key]))
    min_latency.append(min(latencies[key]))

print(latencies[x_r[-1]])

# print range(min,max,(max-min)/100)

# y_r = np.array(y_r)

# y_r = y_r / temp

fig = plt.figure()

# creating a subplot
axes = fig.subplots(3)

axes[0].plot(avg_latency)
axes[0].set_ylabel("latency(ns)")
temp = axes[0].twinx()
temp.set_ylabel('access times')
temp.set_yscale('log')
temp.plot(y_r,'r')

axes[1].plot(max_latency)
axes[1].set_ylabel("latency(ns)")
temp = axes[1].twinx()
temp.set_ylabel('access times')
temp.set_yscale('log')
temp.plot(y_r,'r')

axes[2].plot(min_latency)
axes[2].set_ylabel("latency(ns)")
temp = axes[2].twinx() 

temp.set_ylabel('access times')
temp.set_yscale('log')
temp.plot(y_r,'r')

# ax1.set_ylim(min(min_latency), max(max_latency))


# plt.title('Inserting data description')
plt.grid(True)

plt.show()
