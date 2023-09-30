from Horse import Horse

class Process:
    def __init__(self, pid, arrival_time, burst_time, completion_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = completion_time
        self.turnaround_time = self.completion_time - self.arrival_time
        self.waiting_time = self.turnaround_time - self.burst_time
        self.horse = Horse(
            'Caballo ' + str(self.pid+1),
            50,
            50 * self.pid + 50,
            600,
            self.burst_time
        )

    def __str__(self):
        return f"{self.pid}\t{self.arrival_time}\t{self.burst_time}\t{self.completion_time}\t{self.turnaround_time}\t{self.waiting_time}"


