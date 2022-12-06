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
                copy_info.append(process_info)
                print("P" + process_info['id'] + " has arrived at " + str(arr_t) + " second.")
    # print(arrival)
    # print(check)
    return arrival, check

#function - compare burst time
def compArr(array):
    return array

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

# function to sort by arrival time
def sort_param(e):
    return e['arrival_time']

#sort by arrival time
info.sort(key=sort_param)

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
copy_info = []

# #sort by arrival time
# info.sort(key=sort_param)

for i in range(size):
    process_info = info[i]
    at = process_info['arrival_time']
    bt = process_info['burst_time']
    i_d = process_info['id']

    if i == 0:
    #check if arrival time sama, tapi diff burst time
       for j in range(size-1):
            copy_pi = info[j+1]
            at_copy = copy_pi['arrival_time']
            bt_copy = copy_pi['burst_time']

            if at == at_copy:
                if bt > bt_copy or bt_copy < bt:
                    temp = info[i]
                    info[i] = info[j+1]
                    info[j+1] = temp
                else:
                    break
            else:
                break

       proinfo = process_info

       proinfo['waiting_time'] = 0
       wt = proinfo['waiting_time']
       bt = proinfo['burst_time']
       time += bt

       print("")
       print(info)
       print("P" + proinfo['id'] + "(" + str(bt) + ")")       
       print("Waiting Time: " + str(wt))
       print("Total Time Executed: " + str(time))

       #check whether a process arrived
       print("")
       checkArr(em_arr, sec_arr)


    else:
        proinfo = info[i]
        proinfo['waiting_time'] = time-proinfo['arrival_time']
        wt = proinfo['waiting_time']
        time += bt

        print("")
        print("P" + proinfo['id'] + "(" + str(bt) + ")")
        print("Waiting Time: " + str(wt))
        print("Total Time Executed: " + str(time))

        #check whether a process arrived
        print("")
        checkArr(em_arr, sec_arr)