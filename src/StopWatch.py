import time


class StopWatch:
    """Counts time"""
    def __init__(self):
        self.start = time.time()

    def get_elapsed_time(self):
        return time.strftime("%H:%M:%S", time.gmtime(time.time() - self.start))

    def get_elapsed_time_seconds(self):
        return time.time() - self.start

