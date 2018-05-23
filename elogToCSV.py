#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Antonio Guillen-Perez
@email: antonio.guillen@edu.upct.es
license = see License
version = 1.0
status = production

"""

import numpy as np
import csv

# For an example of usage, use this file_to_open (WE1-64-Tprobe-64-20.elog)
Tprobe = '64-20'
real_num_devices = '64'

file_to_open = 'WE1-' + real_num_devices + '-Tprobe-'+ Tprobe + '.elog'

lines = []

tx_frames_raw = []
tx_frames = []
tx_index = []
tx_columns = []

rx_frames_raw = []
rx_frames_raw_2 = []
rx_frames = []
rx_index = []
rx_columns = []


with open (file_to_open, 'rt') as in_file:  #Open file file_to_open.elog for reading data.
    for line in in_file: #For each line of text store in a string variable named "line", and
        lines.append(line)  #add that line to our list of lines.
        
    # I will extract and save into .csv file some information from this lines
    # This is an application where are transmisor and receptor, so, I will need two files .cvs
    # From here, your application can change a lot of, but this is an example of usage, you must adapt it for your application
    tx_index = [i for i, s in enumerate(lines) if '].wlan[0].mgmt: Sending Probe Request' in s]
    rx_index = [i for i, s in enumerate(lines) if '.wlan.radio: Reception started: attempting' in s]
    in_file.close()

# 
for line in tx_index:
    tx_frames_raw.append([lines[line-3] + lines[line].replace(".", " ")])
tx_columns = list(zip(*(str(row).strip().split(" ") for row in tx_frames_raw)))
tx_frames = np.asmatrix(tx_columns)[(13,4),:]

for line in rx_index:
    rx_frames_raw.append(lines[line])
rx_frames_raw_2 = [elem.replace(',' ,' ')  for elem in rx_frames_raw]
rx_frames_rawDD = [elem.replace('.' ,' ')  for elem in rx_frames_raw]

rx_columns = list(zip(*(row.strip().split(" ") for row in rx_frames_raw_2)))
rx_columns_2 = [i.split(' ')[3] for i in rx_frames_rawDD] 

rx_frames = np.row_stack((rx_columns_2, np.asmatrix(rx_columns)[(13,36,28),:]))


#%% I will save in .csv format the rx_frames and tx_frames variables
# You can save other variables by changing the variable res
# Here is the magic, here I save the variables in .csv format

# First the variable rx_frames
res = rx_frames
csvfile = file_to_open.replace('.elog','-') + 'rx_frames'

"""
#Assuming res is a flat list
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in res:
        writer.writerow([val])    
        
"""

#Assuming res is a list of lists
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(np.transpose(res))


# now tx_frames
res = tx_frames
csvfile = file_to_open.replace('.elog','-') + 'tx_frames'

with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(np.transpose(res))