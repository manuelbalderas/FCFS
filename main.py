from Process import Process

process_data = [
    (0, 3),
    (1, 5),
    (3, 2),
    (9, 5),
    (12, 5)
]

processes = []
completion_time = 0
average_burst_time = 0
average_turnaround_time = 0
average_waiting_time = 0

for pid, data in enumerate(process_data):
    arrival_time, burst_time = data
    completion_time += burst_time
    processes.append(Process(pid, arrival_time, burst_time, completion_time))

print("PID\tAT\tBT\tCT\tTAT\tWT")
for process in processes:
    average_burst_time += process.burst_time
    average_turnaround_time += process.turnaround_time
    average_waiting_time += process.waiting_time
    print(process)

print('\t' * 2 + str(average_burst_time/len(processes)) + '\t' * 2 + str(average_turnaround_time/len(processes)) + '\t' + str(average_waiting_time/len(processes)))

for process in processes:
    print(process.horse)
