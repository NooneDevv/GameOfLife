# This code is made available under the Creative Commons Zero 1.0 License (https://creativecommons.org/publicdomain/zero/1.0)
"""A helper class to assist with counting time."""
import time


class StopWatch(object):
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
