import threading
import time


class RateLimiter:
    

    def __init__(self, requests_per_second: float):
        if requests_per_second <= 0:
            raise ValueError("requests_per_second must be positive")
        self.interval = 1.0 / requests_per_second
        self.next_available_time = 0.0
        self.lock = threading.Lock()

    def wait(self) -> float:
    
        with self.lock:
            now = time.monotonic()
            # If idle, start slot at 'now'; otherwise reserve the next available slot
            target_time = max(now, self.next_available_time)
            sleep_time = target_time - now
            # Advance schedule for the next request
            self.next_available_time = target_time + self.interval

        # Sleep outside the lock so other threads can reserve their slots concurrently
        if sleep_time > 0:
            time.sleep(sleep_time)

        return sleep_time

    def __enter__(self):
  
        self.wait()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass