#!/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.animation as animation

import numpy as np
import random

fig = plt.figure()
#creating a subplot 
ax1 = fig.add_subplot(1,1,1)

data = open('run_log_distribution.txt','r')
line = data.readline()
max = 0
min = 0xffffffffffffffff

values = []
x = 0

couting = {}

while line:
    value = line.split(',')[1] # Delimiter is comma    
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
for key in sorted(couting.keys()):
    temp += couting[key]
    y_r.append(temp)
    x_r.append(key)

# print range(min,max,(max-min)/100)

y_r = np.array(y_r)

y_r = y_r / temp

ax1.clear()
ax1.scatter(x_r,y_r)

plt.xlabel('x')
plt.ylabel('y')
# plt.yscale('log')
plt.title('Inserting data description')	
plt.grid(True)

plt.show()