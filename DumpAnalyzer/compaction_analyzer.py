#!/usr/bin/python3

import re
import json
import numpy as np
from matplotlib import pyplot as plt
from celluloid import Camera

levels = 7
def counting_file(level_vector):
    return len(level_vector)


def parse_level(level_vector):
    result_matrix = []
    for unit in level_vector:
        unit_info = []
        for string in parse_tuple(unit):
            unit_info.append(int(string))
        result_matrix.append(unit_info)
    return result_matrix
        
def parse_tuple(unit):
    unit = unit.replace("{","")
    unit = unit.replace("}","")
    unit = unit.split(",")
    # now it becomes [path, name, access_time, hit_time]
    return unit

LOG_NAME = "LOG"
f = open(LOG_NAME, "r")

line = f.readline()

lsm_states = []

while line:
    log_determin = re.search('(\{.+\})', line)
    if log_determin:
        log_json = json.loads(log_determin.group(0))
        if log_json['event'] == "compaction_finished" or log_json['event'] == "flush_finished":
            lsm_states.append(log_json['lsm_state'])
    line = f.readline()

load_operation_count = len(lsm_states)

LOG_NAME = "LOG_AFTER_READ"
f = open(LOG_NAME, "r")

line = f.readline()

while line:
    log_determin = re.search('(\{.+\})', line)
    if log_determin:
        log_json = json.loads(log_determin.group(0))
        if log_json['event'] == "compaction_finished" or log_json['event'] == "flush_finished":
            lsm_states.append(log_json['lsm_state'])
    line = f.readline()

# finish loading

# find the deepest level
last_frag = lsm_states[-1]
for level in range(1,levels):
    if counting_file(last_frag['level '+ str(level)]) == 0:
        levels = level
        break

# end finding the deepest level


# start ploting
fig, axes = plt.subplots(levels,2)
compaction_times = range(len(lsm_states))
level_vector = range(levels)

first_column_subplots = axes[:,0]

level_num = []
# start file counting
for i in compaction_times:
    frame = []
    for level in level_vector:
        frame.append(counting_file(lsm_states[i]['level '+ str(level)]))
    level_num.append(frame)

frame_matrix = np.matrix(level_num).T

count = 0
for figure in first_column_subplots:
    # figure.axis('off')
    # figure.plot([count]*10)
    # print([count]*10)
    figure.plot(frame_matrix[count].tolist()[0])
    figure.set_ylabel("files count")
    count+=1

# end file counting

# start access time counting
second_column_subplots = axes[:,1]

unit_info_matrix = []



for i in range(load_operation_count,len(lsm_states)):
    frame = {}
    for level in level_vector:
        frame[level] = parse_level(lsm_states[i]['level '+ str(level)])
    unit_info_matrix.append(frame)

level = 0
for time_count_plot in second_column_subplots:
    # collect data from each frame
    access_time_vector = []
    hit_time_vector = []
    hit_ratio = []
    for frame in unit_info_matrix:
        access_time_current_level = 0
        hit_time_current_level = 0
        for sst_record in frame[level]:
            access_time_current_level += sst_record[2]
            hit_time_current_level += sst_record[3]
        access_time_vector.append(access_time_current_level)
        hit_time_vector.append(hit_time_current_level)
        if access_time_current_level != 0:
            hit_ratio.append(float(hit_time_current_level)/float(access_time_current_level))
        else:
            hit_ratio.append(0)
    # access_time_vector.remove(0)
    # hit_time_vector.remove(0)

    time_count_plot.plot(access_time_vector)
    time_count_plot.plot(hit_time_vector,'r')

    time_count_plot.set_ylabel('times')
    
    hit_ratio_plot = time_count_plot.twinx()
    hit_ratio_plot.set_ylabel('hit ratio')
    hit_ratio_plot.set_ylim(-0.2,1.2)
    hit_ratio_plot.plot(hit_ratio,'g',linestyle='dashed')
    level += 1

# end access time counting


# # start hit time counting
# third_column_subplots = axes[:,2]

# unit_info_matrix = []



# for i in range(load_operation_count,len(lsm_states)):
#     frame = {}
#     for level in level_vector:
#         frame[level] = parse_level(lsm_states[i]['level '+ str(level)])
#     unit_info_matrix.append(frame)

# print(unit_info_matrix[0])
# level = 0
# for figure in third_column_subplots:
#     # collect data from each frame
#     access_time_vector = []

#     for frame in unit_info_matrix:
#         access_time_current_level = 0
#         for sst_record in frame[level]:
#             access_time_current_level += sst_record[3]
#         access_time_vector.append(access_time_current_level)

#     figure.plot(range(load_operation_count,len(lsm_states)),access_time_vector)
#     level += 1
# # end hit time counting



plt.show()