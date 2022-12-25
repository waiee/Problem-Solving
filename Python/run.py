def ganttChart(bar, time, processName):
    print("Gantt Chart: \n")
    print("*--------", end="")
    for i in range(bar-1):
        print("---------",end="")
    print("*")

    for i in range(bar):
        print(f'{("|   "+ "P" + processName[i] +"  "):9.7}',end="")
    print("|")

    print("*--------",end="")
    for i in range(bar-1):
        print("---------",end="")
    print("*")

    for i in range(len(time)):
        print(f'{(str(time[i])+"       "):9.3}',end="")
    time.pop(0)
    print("\n")

def printProcess(id, bt, time):
    for i in range(size):
        print("P" + str(id[i]) + "(" + str(bt[i]) + ")")
        print("Total time executed: " + str(time[i]) + " second")
        print("")

def calculate(para1, para2, para3):
    para1 = para2-para3
    return para3 

def totalAv(total, time):
    total += time
    return total

# User insert number of process
print("[Non-Preemptive SJF] \n")
while True:
    n = int(input("Enter number of processes: "))
    if n < 3 or n > 10:
        print("Please enter number from 3-10.")
    else:
        break
print("")

#Define
size = n
info = []
copy_info = []
final_info = []
totalTime = 0

#User input
for i in range(size):
    process_info = {}
    print("[P" + str(i) + "]")
    process_info['id'] = str(i)
    process_info['burst_time'] = int(input("Enter Burst Time: "))
    process_info['arrival_time'] = int(input("Enter Arrival Time: "))
    process_info['waiting_time'] = 0
    process_info['turnaround_time'] = 0
    info.append(process_info)
    totalTime += info[i]['burst_time']
    print("")

#Sort by arrival time
def sort_param(e):
    return e['arrival_time']

#Sort by burst time
def sort_burst(e):
    return e['burst_time']

# Menu
print("---------------------------------------------")
print("{:<15} {:<15} {:<15}".format('Process', 'Burst Time', 'Arrival Time'))
for i in range(size):
    p = info[i]
    print("{:<15} {:<15} {:<15}".format(
        p['id'], p['burst_time'], p['arrival_time']))
print("---------------------------------------------")

# Algorithm
time = 0
wt = 0
tt = 0
timeFrame = [0]
finalID = []
finalBt = []
totalTt = 0
totalWt = 0

info.sort(key=sort_param)
for i in range(totalTime): 
    for j in range(size): 
        if info[j]['arrival_time'] == i:
            copy_info.append(info[j])
        else:
            copy_info.sort(key=sort_burst)
            for n in range(len(copy_info)):
                final_info.append(copy_info[n])
            copy_info.clear()

for i in range(size):
    print_info = final_info[i]
    time += print_info['burst_time']
    timeFrame.append(time)
    finalID.append(print_info['id'])
    finalBt.append(print_info['burst_time'])

    # print_info['turnaround_time']=time-print_info['arrival_time']
    calculate(print_info['turnaround_time'], time, print_info['arrival_time'])
    # totalTt += print_info['turnaround_time']
    totalAv(totalTt, print_info['turnaround_time'])
    # print_info['waiting_time']=print_info['turnaround_time']-print_info['burst_time']
    calculate(print_info['waiting_time'], print_info['turnaround_time'], print_info['burst_time'])
    # totalWt += print_info['waiting_time']
    totalAv(totalWt, print_info['waiting_time'])

#Output
print("\n")
ganttChart(size, timeFrame, finalID)
printProcess(finalID, finalBt, timeFrame)
print("Total Turnaround Time: " + str(totalTt))
print("Total Waiting Time: " + str(totalWt))