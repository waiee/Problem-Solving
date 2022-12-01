import numpy as np

#function - check arrival
def checkArr(arrival):
    for i in range(size):
        process_info = info[i]
        arrival_info = process_info['arrival_time']
        if arrival_info <= time:
            if arrival_info in sec_arr:
                em_arr.append(arrival_info)
                sec_arr.pop(arrival_info)
                print("P" + str(i) + " has arrived.")
            else:
                break
            
    
    print(em_arr)
    print(sec_arr)
    return arrival

#function - check arrival != 0
# def checkArr2(arrival):
#     for i in range(size):
#         process_info = info[i]
#         if process_info['arrival_time'] <= time:
#             for j in range(size):

#                 em_arr.append(i)
#                 print("P" + str(i) + " has arrived.")

#     print(em_arr)
#     print(sec_arr)
#     return arrival

# def fill_arr(array):
#     for i in range(size):
#         for j in range(size):
#             sec = sec_arr[j]
#             if em_arr[i] == sec:
#                 break
#             else:
#                 em_arr.append(i)
#     return array       

# User insert number of process
n = int(input("Enter number of processes: "))
print("")

info = []
bt = 0
size = n+1

for i in range(size):
    process_info = {}
    print("[P" + str(i) + "]")
    process_info['id'] = str(i)
    process_info['burst_time'] = int(input("Enter Burst Time: "))
    process_info['arrival_time'] = int(input("Enter Arrival Time: "))

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

####### fill array for checking ######
em_arr = []*size
sec_arr = []*size

for i in range(size):
    process_info = info[i]
    arrival_info = process_info['arrival_time']
    sec_arr.append(arrival_info)

# Algorithm
time = 0
wt = 0
bt = 0
check_Arr = 0

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
    #    fill_arr(em_arr)
       checkArr(check_Arr)

    
    else:
        process_info['waiting_time'] = time-process_info['arrival_time']
        wt = process_info['waiting_time']
        time += bt

        print("Waiting Time: " + str(wt))
        print("Total Time Executed: " + str(time))

        #check whether a process arrived
        print("")
        # fill_arr(em_arr)
        # checkArr2(check_Arr)