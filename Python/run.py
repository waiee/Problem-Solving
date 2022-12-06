import numpy as np

# User insert number of process
print("[Non-Preemptive SJF] \n")
while True:
    n = int(input("Enter number of processes: "))
    if n < 3 or n > 10:
        print("Please enter number from 3-10.")
    else:
        break
print("")

#define
bt = 0
size = n
info = []
copy_info = []
final_info = []
bt = 0

for i in range(size):
    process_info = {}
    print("[P" + str(i) + "]")
    process_info['id'] = str(i)
    process_info['burst_time'] = int(input("Enter Burst Time: "))
    process_info['arrival_time'] = int(input("Enter Arrival Time: "))
    process_info['waiting_time'] = 0
    info.append(process_info)
    bt += info[i]['burst_time']
    print("")

# function to sort by arrival time
def sort_param(e):
    return e['arrival_time']
info.sort(key=sort_param)

# function to sort by burst time
def sort_burst(e):
    return e['burst_time']

# Menu
print("{:<15} {:<15} {:<15}".format('Process', 'Burst Time', 'Arrival Time'))

for i in range(size):
    p = info[i]
    print("{:<15} {:<15} {:<15}".format(
        p['id'], p['burst_time'], p['arrival_time']))

# Algorithm
time = 0
wt = 0

for i in range(bt): #start at 0 second
    for j in range(size):
        if info[j]['arrival_time'] == i:
            copy_info.append(info[j])
        else:
            copy_info.sort(key=sort_burst)
            for n in range(len(copy_info)):
                final_info.append(copy_info[n])
            copy_info.clear()

print(final_info)
print("Total time executed: " + str(bt))