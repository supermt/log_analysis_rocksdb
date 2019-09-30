#!/usr/bin/python

# import re
# import json
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict


INDEX_NAME = "index_file_snappy_compression.csv"

f = open(INDEX_NAME, "r")

lines = f.readlines()

xs = []
ys = []

d={}
for line in lines:
    kv = line.split(",")
    x = long(kv[0].ljust(48, '0'))
    y = long(kv[1].replace("\n",""),16)
    
    # if y_c > y:
    #     print kv[1].replace("\n","")
    #     break

    xs.append(x)
    ys.append(y)
    d[x]=y

# fig, axs = plt.subplots(2, 5)

# # 0~4 first row
# # 5~9
# window = 160
# for row in range(2):
#     start = 0 +( 5 * window * row )
#     for column in range(5):
#         start += window/2
#         keyrange = ys[start:start+window]

#         axs[row][column].set_title("start point: " + str(start) + 
#         "\nomwindow size " + str(window) + 
#         "\n space range " + '%.2E' % (max(keyrange) - min(keyrange)),
#         fontsize=10)
#         axs[row][column].scatter(xs[start:start+window],ys[start:start+window])

# window = 40
# start = 600

# fig.suptitle('window size = ' + str(window), fontsize=16)

# y_x_pair = OrderedDict(sorted(d.items(), key=lambda x: x[1]))
# plt.scatter(xs[start:start+window],ys[start:start+window])

plt.plot(xs[0:300])
plt.twinx().plot(ys[0:300],'r')

plt.show()