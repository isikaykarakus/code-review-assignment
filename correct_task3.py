# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.

def average_valid_measurements(values):
    total = 0
    count = 0 # Change: Start at 0
    for v in values:
        if v is not None:
            total += float(v)
            count += 1 # Change: Only increment for non-None values
    return total / count if count > 0 else 0 # Change: Avoid division by zero, return 0 if no valid measurements