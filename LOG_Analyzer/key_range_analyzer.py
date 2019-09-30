#!/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.animation as animation

import numpy as np
import random

fig = plt.figure()
#creating a subplot 
ax1 = fig.add_subplot(1,1,1)

data = open('run_log_new.txt','r')
line = data.readline()
max = 0
min = 0xffffffffffffffff

values = []
x = 0

couting = {}

while line:
    value = line.split(',')[1] # Delimiter is comma
    if line.split(',')[0]=="Point":
        latency = line.split(',')[2]
    value = long(value.replace("user",""))
    if value > max:
        max = value
    if value < min:
        min = value
    couting[value] = couting.get(value,0) + 1 
    
    line = data.readline()

x_r = []
y_r = []
temp = 0.0
for key, value in sorted(couting.items(), key=lambda item: item[1]):
    # temp += couting[key]
    x_r.append(key)
    y_r.append(value)

# print range(min,max,(max-min)/100)

# y_r = np.array(y_r)

# y_r = y_r / temp

ax1.clear()
ax1.plot(y_r)
ax1.set_xlabel('key')
ax1.set_ylabel('access times')
ax1.set_yscale('log')

# plt.xlabel('x')
# plt.ylabel('y')
# plt.yscale('log')
plt.title('Inserting data description')	
plt.grid(True)

plt.show()