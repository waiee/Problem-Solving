n=int(input('Enter number of processes : '))

print('Enter process id, burst time and priority in order of arrival:')

info=[]

total_wt_time=0

total_ta_time=0

for i in range(n):

    l=input().split()

    process_info={}

    process_info['id']=l[0]

    process_info['burst_time']=float(l[1])

    process_info['priority']=int(l[2])

    if i==0:

        process_info['wait_time']=0

    else:

        process_info['wait_time']=info[i-1]['wait_time']+info[i-1]['burst_time']



    process_info['turnaround_time']=process_info['wait_time']+process_info['burst_time']



    total_wt_time+=process_info['wait_time']

    total_ta_time+=process_info['turnaround_time']



    info.append(process_info)



print('\nFCFS:')

print("{:<15} {:<15} {:<15} {:<20}".format('Process_id','Burst_time','Wait_time','Turnaround_time'))

for i in range(n):

    p=info[i]

    print("{:<15} {:<15} {:<15} {:<20}".format(p['id'],p['burst_time'],p['wait_time'],p['turnaround_time']))



avg_wt_time=total_wt_time/n

avg_ta_time=total_ta_time/n

print('Average waiting time : ',avg_wt_time)

print('Average turnaround time : ',avg_ta_time)



print('\n\nShortest Job First (SJF):')

def sort_param(e):

    return e['burst_time']

info.sort(key=sort_param)

total_wt_time=0

total_ta_time=0

for i in range(n):

    process_info=info[i]

    if i==0:

        process_info['wait_time']=0

    else:

        process_info['wait_time']=info[i-1]['wait_time']+info[i-1]['burst_time']



    process_info['turnaround_time']=process_info['wait_time']+process_info['burst_time']



    total_wt_time+=process_info['wait_time']

    total_ta_time+=process_info['turnaround_time']

    

print("{:<15} {:<15} {:<15} {:<20}".format('Process_id','Burst_time','Wait_time','Turnaround_time'))

for i in range(n):

    p=info[i]

    print("{:<15} {:<15} {:<15} {:<20}".format(p['id'],p['burst_time'],p['wait_time'],p['turnaround_time']))



avg_wt_time=total_wt_time/n

avg_ta_time=total_ta_time/n

print('Average waiting time : ',avg_wt_time)

print('Average turnaround time : ',avg_ta_time)



print('\n\nPriority scheduling:')

def sort_param2(e):

    return e['priority']

info.sort(key=sort_param2)

total_wt_time=0

total_ta_time=0

for i in range(n):

    process_info=info[i]

    if i==0:

        process_info['wait_time']=0

    else:

        process_info['wait_time']=info[i-1]['wait_time']+info[i-1]['burst_time']



    process_info['turnaround_time']=process_info['wait_time']+process_info['burst_time']



    total_wt_time+=process_info['wait_time']

    total_ta_time+=process_info['turnaround_time']

    

print("{:<15} {:<15} {:<15} {:<15} {:<20}".format('Process_id','Burst_time','Wait_time','Priority','Turnaround_time'))

for i in range(n):

    p=info[i]

    print("{:<15} {:<15} {:<15} {:<15} {:<20}".format(p['id'],p['burst_time'],p['wait_time'],p['priority'],p['turnaround_time']))



avg_wt_time=total_wt_time/n

avg_ta_time=total_ta_time/n

print('Average waiting time : ',avg_wt_time)

print('Average turnaround time : ',avg_ta_time)