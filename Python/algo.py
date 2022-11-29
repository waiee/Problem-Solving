

#Enter number or processes
np = int(input("Enter number of processes: "))

#loop for arrival time, burst time
position = []
arrival_time = []
burst_time = []

for i in range(np):
    position.append(i+1)
    arrival_time.append(int(input("Enter arrival time for P" + str(i+1) + ": ")))

print("---------------------------------")
print("Process   Arrival time")
print("P" + str(position[0]) + "        " + str(arrival_time[0]))




