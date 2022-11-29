# import numpy as np

# #Enter number or processeswhile True:
# np = int(input("Enter number of processes: "))

#loop for arrival time, burst time
# position = []
# arrival_time = []  
# burst_time = []

# def sorted(arr):
#     arrival_time.sort()
#     return arr

# for i in range(np):
#     position.append(i+1)
#     arrival_time.append(int(input("Enter arrival time for P" + str(i+1) + ": ")))
#     burst_time.append(int(input("Enter burst time for P" + str(i+1) + ": ")))

# sorted(arrival_time)
# # print(arrival_time)

# #menu
# print("---------------------------------")
# print("Process   Arrival Time   Burst Time")
# for i in range(len(position)):
#     print("P" + str(position[i]) + "        " + str(arrival_time[i]) +
#      "\t\t " + str(burst_time[i]))

import numpy as np

np=int(input("Enter number of processes: "))

info = []

total_wt = 0
total_ta = 0

for i in range(np):
    process_info = {}
    process_info['id'] = str(i+1)
    process_info['arrival_time'] = int(input("Enter arrival time for P" + str(i+1) + ": "))
    process_info['burst_time'] = int(input("Enter burst time for P" + str(i+1) + ": "))

    info.append(process_info)

print("{:<15} {:<15} {:<15}".format('Process','Arrival Time','Burst Time'))

for i in range(np):

    p=info[i]

    print("{:<15} {:<15} {:<15}".format(p['id'],p['arrival_time'],p['burst_time']))






