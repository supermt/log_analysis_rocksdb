#!/usr/bin/python

# import re
# import json
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict


INDEX_NAME = "index_file.csv"

f = open(INDEX_NAME, "r")

line = f.readline()

xs = []
ys = []

y_c = 0
d={}
while line:
    kv = line.split(",")
    x = long(kv[0].ljust(48, '0'))
    y = long(kv[1].replace("\n",""),16)
    
    # if y_c > y:
    #     print kv[1].replace("\n","")
    #     break

    xs.append(x)
    ys.append(y)
    line = f.readline()
    y_c = y

    d[x]=y

d = sorted(d.items(), key = lambda kv:(kv[1], kv[0]))
xs=[]
ys=[]
for entry in d:
    if entry[1] >= 150000000000000L:
        xs.append(entry[0])
        ys.append(entry[1])

fig, axs = plt.subplots(2, 5)

# 0~4 first row
# 5~9

for row in range(2):
    start = 500 + row * 100 
    for column in range(5):
        window = 20 * (2 ** column)
        keyrange = ys[start:start+window]

        axs[row][column].set_title("start point: " + str(start) + 
        "\nomwindow size " + str(window) + 
        "\n space range " + '%.2E' % (max(keyrange) - min(keyrange)),
        fontsize=10)
        axs[row][column].scatter(xs[start:start+window],ys[start:start+window])

# window = 40
# start = 600

# fig.suptitle('window size = ' + str(window), fontsize=16)

# y_x_pair = OrderedDict(sorted(d.items(), key=lambda x: x[1]))
# plt.scatter(xs[start:start+window],ys[start:start+window])

# plt.plot(xs,ys)

plt.show()