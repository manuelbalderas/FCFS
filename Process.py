from Horse import Horse


class Process:
    def __init__(self, pid, arrival_time, burst_time, completion_time, distance):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = completion_time
        self.turnaround_time = self.completion_time - self.arrival_time
        self.waiting_time = max(self.turnaround_time - self.burst_time, 0)
        self.entry_time = self.arrival_time + self.waiting_time
        self.horse = Horse(
            (15, 150 * self.pid + 50),
            distance,
            self.burst_time
        )

    def __str__(self, scale_factor):
        return f"{self.pid}\t{int(self.arrival_time/scale_factor)}\t{int(self.burst_time/scale_factor)}\t{int(self.completion_time/scale_factor)}\t{int(self.turnaround_time/scale_factor)}\t{int(self.waiting_time/scale_factor)}"
