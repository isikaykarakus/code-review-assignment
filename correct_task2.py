# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.

def count_valid_emails(emails):
    count = 0

    for email in emails:
        # Change: skip non-strings to avoid type error on `"@" in emails
        if not isinstance(email, str):
            continue
        # Change: require exactly one '@' not just "contains"
        if email.count("@") != 1:
            continue
        # Change: require non-empty local and domain parts
        local, domain = email.split("@")
        if local and domain:
            count += 1
    return count
