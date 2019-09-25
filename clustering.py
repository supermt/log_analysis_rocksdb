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

# best_partition = 1024*1024*500

best_partition = 4 * 1024

steps = []
y_c = ys[0]
for y in ys:
    steps.append(y-y_c)
    y_c = y

plt.plot(steps)
plt.show()
