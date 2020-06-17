# python3
# Input: The number of threads (n_workers), the number of jobs (n_jobs), and the time to complete these jobs (jobs)
# Output: The thread assigned and the time it will start the job

import heapq

class Worker:
    def __init__(self, thread_id, release_time=0):
        self.thread_id = thread_id
        self.release_time = release_time

    def __lt__(self, other):
        if self.release_time == other.release_time:
            return self.thread_id < other.thread_id
        return self.release_time < other.release_time

    def __gt__(self, other):
        if self.release_time == other.release_time:
            return self.thread_id > other.thread_id
        return self.release_time > other.release_time

def assign_jobs(n_workers, jobs):
    result = []
    worker_queue = [Worker(i) for i in range(n_workers)]
    for job in jobs:
        worker = heapq.heappop(worker_queue)
        result.append((worker.thread_id, worker.release_time))
        worker.release_time += job
        heapq.heappush(worker_queue, worker)
    return result

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job[0], job[1])

if __name__ == "__main__":
    main()
