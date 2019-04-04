#!/usr/bin/python

import os
import sys
import time
import subprocess

if len(sys.argv) > 1:
    time_window = sys.argv[1]
else:
    time_window = '2'

# get the interface
output = subprocess.check_output(["ip", "link", "show"])
output = output.strip('\n').split('\n')
output = [line.split()[1].strip(':') for line in output]

count = 0
for i in output:
    if count == 0:
        if i[0] == 'e':
            iface = i
    count = (count + 1) % 2

while True:
    print "-------------------------------------------------------------------"
    output = subprocess.check_output(["sudo", "iftop", "-i", iface, "-t", "-s",\
            time_window])
    output = output.strip('\n').split('\n')
    id_1 = 0
    id_2 = 0
    id_3 = 0
    for i in xrange(len(output)):
        if output[i][:3] == "---":
            if not id_1:
                id_1 = i
            elif not id_2:
                id_2 = i
            elif not id_3:
                id_3 = i
    lines = output[id_1:id_2+1]

    lines.pop(0)
    while len(lines) > 1:
        one = lines.pop(0).split()
        two = lines.pop(0).split()

        one.pop(0)

        if one[0].split('.')[0][:3] == "192" or two[0].split('.')[0][:3] == "192":
            print ' '.join(two[:3])+"ps"
            print
    print "==================================================================="
    print
