import numpy as np

#function - check arrival
def checkArr(arrival, check):
    for i in range(size):
        process_info = info[i]
        arr_t = process_info['arrival_time']
        if arr_t <= time:
            if arr_t in sec_arr:
                arrival.append(arr_t)
                check.remove(arr_t)
                print("P" + str(i) + " has arrived.")
            else:
                break
    print(arrival)
    print(check)
    return arrival, check

# User insert number of process
n = int(input("Enter number of processes: "))
print("")

info = []
bt = 0
size = n

####### array for checking arrival ######
em_arr = []*size
sec_arr = []*size

for i in range(size):
    process_info = {}
    print("[P" + str(i) + "]")
    process_info['id'] = str(i)
    process_info['burst_time'] = int(input("Enter Burst Time: "))
    process_info['arrival_time'] = int(input("Enter Arrival Time: "))
    sec_arr.append(process_info['arrival_time'])

    info.append(process_info)
    print("")

# Sort by arrival time
# def sort_param(e):
#     return e['arrival_time']
# info.sort(key=sort_param)

# Menu
print("{:<15} {:<15} {:<15}".format('Process', 'Burst Time', 'Arrival Time'))

for i in range(size):
    p = info[i]
    print("{:<15} {:<15} {:<15}".format(
        p['id'], p['burst_time'], p['arrival_time']))

# Algorithm
time = 0
wt = 0
bt = 0

for i in range(size):
    process_info = info[i]
    bt = process_info['burst_time']

    print("") 
    print("P" + str(i) + "(" + str(bt) + ")") 

    if i == 0:
       process_info['waiting_time'] = 0
       wt = process_info['waiting_time']
       time += bt

       print("Waiting Time: " + str(wt))
       print("Total Time Executed: " + str(time))

       #check whether a process arrived
       print("")
       checkArr(em_arr, sec_arr)

    
    else:
        process_info['waiting_time'] = time-process_info['arrival_time']
        wt = process_info['waiting_time']
        time += bt

        print("Waiting Time: " + str(wt))
        print("Total Time Executed: " + str(time))

        #check whether a process arrived
        print("")
        checkArr(em_arr, sec_arr)
        