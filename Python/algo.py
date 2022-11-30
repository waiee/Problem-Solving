import numpy as np

# User insert number of process
n = int(input("Enter number of processes: "))
print("")

info = []
total_wt = 0
total_ta = 0
bt = 0

for i in range(n):
    process_info = {}
    print("[P" + str(i) + "]")
    process_info['id'] = str(i)
    process_info['burst_time'] = int(
        input("Enter Burst Time: "))
    process_info['arrival_time'] = int(
        input("Enter Arrival Time: "))

    info.append(process_info)
    print("")

# Sort by arrival time
def sort_param(e):
    return e['arrival_time']
info.sort(key=sort_param)

# Menu
print("{:<15} {:<15} {:<15}".format('Process', 'Burst Time', 'Arrival Time'))

for i in range(n):
    p = info[i]
    print("{:<15} {:<15} {:<15}".format(
        p['id'], p['burst_time'], p['arrival_time']))



# Algorithm
# time = 0
# total_time = 0
# bt = 0

# for i in range(np):
#     process_info = info[i]

#     if i==0:
#         # process_info['wait_time'] = 0
#         bt = process_info['burst_time']
#         time+= bt

#     else: 



