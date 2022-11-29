

#Enter number or processes
np = int(input("Enter number of processes: "))

#loop for arrival time, burst time
arrival_time = []
burst_time = []

for i in range(np):
    arrival_time.append(int(input("Enter arrival time for P" + i)))
