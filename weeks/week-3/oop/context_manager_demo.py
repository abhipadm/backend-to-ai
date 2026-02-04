
class UsageTracker:

    count = 0

    def __enter__(self):
        UsageTracker.count += 1
        print(f"Entering context: count = {UsageTracker.count}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        UsageTracker.count -= 1
        print(f"Exiting context: count = {UsageTracker.count}") 

from contextlib import contextmanager
@contextmanager
def UsageTrackerWithLib():
    UsageTracker.count += 1
    print(f"Entering context: count = {UsageTracker.count}")
    try:
        yield
    finally:
        UsageTracker.count -= 1
        print(f"Exiting context: count = {UsageTracker.count}")

if __name__ == "__main__":
    print("Context Manager Manual Demo\n")
    
    print("Starting outer context")
    with UsageTracker() as tracker1:
        print("Inside outer context")
        print("Starting inner context")
        with UsageTracker() as tracker2:
            print("Inside inner context")
        print("Exited inner context")
    print("Exited outer context")

    print("\nContext Manager with contextlib Demo\n")
    print("Starting outer context")
    with UsageTrackerWithLib():
        print("Inside outer context")
        print("Starting inner context")
        with UsageTrackerWithLib():
            print("Inside inner context")
        print("Exited inner context")
    print("Exited outer context")