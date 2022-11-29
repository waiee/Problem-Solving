import numpy as np

# User insert number of process
np = int(input("Enter number of processes: "))
print("")

info = []
total_wt = 0
total_ta = 0

for i in range(np):
    process_info = {}
    print("(P" + str(i+1) + ")")
    process_info['id'] = str(i+1)
    process_info['arrival_time'] = int(
        input("Enter Arrival Time: "))
    process_info['burst_time'] = int(
        input("Enter Burst Time: "))

    info.append(process_info)
    print("")

# Sort by arrival time
def sort_param(e):
    return e['arrival_time']
    
info.sort(key=sort_param)

# Menu
print("{:<15} {:<15} {:<15}".format('Process', 'Arrival Time', 'Burst Time'))

for i in range(np):
    p = info[i]
    print("{:<15} {:<15} {:<15}".format(
        p['id'], p['arrival_time'], p['burst_time']))

# Algorithm
