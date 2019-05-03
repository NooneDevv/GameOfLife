import time


class StopWatch:
    """Counts time"""
    def __init__(self):
        self.start = time.time()

    def get_elapsed_time(self):
        """Returns elapsed time in HH:MM:SS format."""
        return time.strftime("%H:%M:%S", time.gmtime(time.time() - self.start))

    def get_elapsed_time_seconds(self):
        """Returns elapsed time in epoch format."""
        return time.time() - self.start

    def reset(self):
        """Resets the start time."""
        self.start = time.time()
