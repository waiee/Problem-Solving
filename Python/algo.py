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
                burst_arr.append(process_info['burst_time'])
                copy_info.append(process_info)
                print("P" + process_info['id'] + " has arrived at " + str(arr_t) + " second.")
    # print(arrival)
    # print(check)
    return arrival, check

#function - delete first array
def delArr(array, array2):
    i = 0
    array.pop(i)
    array.sort()
    array2.pop(i)
    array2.sort(key=sort_burst)
    return array, array2

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
info = []
bt = 0
size = n
em_arr = []*size
sec_arr = []*size
burst_arr = []*size

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

# function to sort by arrival time
def sort_burst(e):
    return e['burst_time']

# info.sort(key=sort_burst)

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

#sort by arrival time
info.sort(key=sort_param)

for i in range(size):
    info.sort(key=sort_param)
    process_info = info[i]
    at = process_info['arrival_time']
    bt = process_info['burst_time']
    i_d = process_info['id']

    if i == 0:
    #check if arrival time sama, tapi diff burst time
       for j in range(size):
            p_i = info[j+1]
            at_pi = p_i['arrival_time']
            bt_pi = p_i['burst_time']
            id_pi = p_i['id']

            if at == at_pi:
                if bt > bt_pi:
                    temp_bt = bt
                    temp_id = i_d
                    bt = bt_pi
                    i_d = id_pi
                    bt_pi = temp_bt
                    id_pi = temp_id
            else:
                break
    
       process_info['waiting_time'] = 0
       wt = process_info['waiting_time']
       time += bt

       print("")
       print(burst_arr)
       print("P" + process_info['id'] + "(" + str(bt) + ")")       

       print("Waiting Time: " + str(wt))
       print("Total Time Executed: " + str(time))

       #check whether a process arrived
       print("")
       checkArr(em_arr, sec_arr)
       delArr(burst_arr, copy_info)
       print(burst_arr)
       print(copy_info)

    else:
        process_info['waiting_time'] = time-process_info['arrival_time']
        wt = process_info['waiting_time']
        time += bt

        print("")
        print(burst_arr)
        print("P" + process_info['id'] + "(" + str(bt) + ")")

        print("Waiting Time: " + str(wt))
        print("Total Time Executed: " + str(time))

        #check whether a process arrived
        print("")
        checkArr(em_arr, sec_arr)
        delArr(burst_arr, copy_info)
        print(burst_arr)