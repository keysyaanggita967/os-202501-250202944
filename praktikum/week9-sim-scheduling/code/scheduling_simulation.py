# FCFS Scheduling Simulation
# Dataset proses
process = ["P1", "P2", "P3", "P4"]
arrival_time = [0, 1, 2, 3]
burst_time = [6, 8, 7, 3]

n = len(process)

start_time = [0] * n
finish_time = [0] * n
turnaround_time = [0] * n
waiting_time = [0] * n

# Proses pertama
start_time[0] = arrival_time[0]
finish_time[0] = start_time[0] + burst_time[0]
turnaround_time[0] = finish_time[0] - arrival_time[0]
waiting_time[0] = turnaround_time[0] - burst_time[0]

# Proses berikutnya (FCFS)
for i in range(1, n):
    start_time[i] = max(finish_time[i - 1], arrival_time[i])
    finish_time[i] = start_time[i] + burst_time[i]
    turnaround_time[i] = finish_time[i] - arrival_time[i]
    waiting_time[i] = turnaround_time[i] - burst_time[i]

# Output tabel
def garis():
    print("+---------+--------------+------------+------------+-------------+------------------+--------------+")

garis()
print("| Process | Arrival Time | Burst Time | Start Time | Finish Time | Turnaround Time | Waiting Time |")
garis()

for i in range(n):
    print(f"| {process[i]:<7} | {arrival_time[i]:<12} | {burst_time[i]:<10} | "
          f"{start_time[i]:<10} | {finish_time[i]:<11} | {turnaround_time[i]:<16} | {waiting_time[i]:<12} |")

garis()

# Rata-rata
print(f"| {'AVERAGE':<7} | {'-':<12} | {'-':<10} | {'-':<10} | {'-':<11} | {sum(turnaround_time)/n:<16.2f} | {sum(waiting_time)/n:<12.2f} |")
garis()
