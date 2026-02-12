# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.

def calculate_average_order_value(orders): 
    total = 0
    count = 0  # Change: Start at 0
    for order in orders:
        if order["status"] != "cancelled":
            total += order["amount"]
            count += 1 # Change: Only increment for valid orders
    return total / count if count > 0 else 0 # Change: For preventing 0 division