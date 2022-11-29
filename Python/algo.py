import numpy as np

np = int(input("Enter number of processes: "))

info = []
total_wt = 0
total_ta = 0

for i in range(np):
    process_info = {}
    process_info['id'] = str(i+1)
    process_info['arrival_time'] = int(
        input("Enter arrival time for P" + str(i+1) + ": "))
    process_info['burst_time'] = int(
        input("Enter burst time for P" + str(i+1) + ": "))

    info.append(process_info)

def sort_param(e):

    return e['arrival_time']

info.sort(key=sort_param)

# Menu
print("{:<15} {:<15} {:<15}".format('Process', 'Arrival Time', 'Burst Time'))

for i in range(np):
    p = info[i]
    print("{:<15} {:<15} {:<15}".format(
        p['id'], p['arrival_time'], p['burst_time']))
