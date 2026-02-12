# AI Code Review Assignment (Python)

## Candidate
- Name: Işıkay Karakuş 
- Approximate time spent: 75 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- Count is the length of the entire list, but total only sums non-cancelled orders. This will result low average when there are cancelled orders. 
- If the input orders list is empty count will be zero, and this will cause a zero division error.

### Edge cases & risks
- If all the orders are cancelled, the count will be zero, which will cause a zero division error even if the list itself is not empty. 

### Code quality / design issues
- It is safer to calculate the count dynamically rather than calculating the length initially. 

## 2) Proposed Fixes / Improvements
### Summary of changes
- The count is set to 0 and incremented only in the if block.
- Added control statement for division by zero error; if the count is zero, it returns zero.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

- All cancelled orders are to ensure that the function returns zero and does not raise an error.
- Test with half of the cancelled orders and half of the valid orders to ensure the average is calculated correctly.
- Pass an empty to list to ensure that the function handles the absence of data without crashing.


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- The function does not "correctly excludes" cancel orders and it does not specify that "number of orders" refers to the entire length of the list, not just the filtered number.

### Rewritten explanation
- The function calculates the average value of active orders. It iterates through the list, summing the amount of any order not marked as "cancelled." To ensure mathematical accuracy, it divides this sum only by the number of valid orders processed, rather than the total size of the input list.

## 4) Final Judgment
- Decision: Approve / **Request Changes**  / Reject
- Justification: The original implementation has a denominator logic bug (it divides by total orders instead of non-cancelled orders) and can raise a division-by-zero error for empty or fully cancelled inputs.
- Confidence & unknowns: Confidence is high that the fix resolves the correctness and divide-by-zero issues; the main unknown is whether orders may have missing or invalid amount or status fields and how those should be handled.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- It does not verify if there is a domain (e.g., .com) or if there are characters before and after the @ symbol.
- The function identifies any string containing @ as a valid email. This would incorrectly count "@@@", "admin@" or "@company" as valid.


### Edge cases & risks
- The function counts any string containing the character, meaning invalid formats like "user@@@com" are incorrectly marked as valid.
- Empty input list is fine but lists containing non-strings will crash.
- Leading and trailing whitespace would be counted as valid without normalisation like " ab@a.com "  or could be considered invalid depending on requirements.
- A single @ symbol at the very start or end of a string is counted as valid, even though it lacks a username or domain.

### Code quality / design issues
- The function’s notion of “valid” is not defined beyond containing “@”; it should at least enforce a consistent minimal rule set.
- There are no type checks and normalisation.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Added a type check to skip non-string entries safely.
- Normalised entries with .strip() to handle accidental surrounding whitespace.
- Replaced the weak "@" in email check with a minimal validity policy:
    - Exactly one “@”
    - Non-empty local part and domain part 
    - Domain contains at least one “.”


### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

- Pass a list containing non-string values (e.g., None, integers) to ensure the function does not crash and safely skips invalid entries.
- Test emails with no @ and with multiple @ (e.g., "abc.com", "a@@b.com") to ensure they are not counted.
- Test emails with empty local or domain parts (e.g., "a@", "@b.com") to ensure they are not counted.
- Test a list with a mix of valid and invalid emails to ensure the final count is correct.
- Pass an empty list to ensure the function returns 0 without errors.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
-  It claims the function "counts valid email addresses" but the function actually only counts strings with an @ symbol. In addition, "safely ignores invalid entries" is misleading because it would actually accept many invalid formats.

### Rewritten explanation
- This function counts emails in the input list using a minimal validity policy: it skips non-strings to avoid errors, trims surrounding whitespace, requires exactly one “@” with non-empty local and domain parts and checks that the domain contains at least one dot.

## 4) Final Judgment
- Decision: Approve / **Request Changes** / Reject
- Justification: The original code can crash and counts invalid emails, so minimal checks were added for safety and correctness.
- Confidence & unknowns: Confidence is high that the function is now safe and correct under the chosen minimal validity rules, but the exact definition of a “valid email” may vary depending on product requirements.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- The original implementation increments the count for every element even when the value is "None", which produces an incorrect average.
- If all values are "None" or the list is empty, the function can divide by zero and crash.

### Edge cases & risks
- If the input list contains only "None" values, the function should return a safe value instead of raising an error.
- If the list contains non-numeric values (e.g., strings that cannot be converted), float(v) can raise an exception.

### Code quality / design issues
- The count should represent only valid measurements rather than the total list length.
- A defensive guard against division by zero is necessary.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Initialized count as 0 and incremented it only when the value is not "None".
- Added a division-by-zero guard for returning 0 when there are no valid measurements.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

- Pass an empty list to ensure the function returns 0 and does not crash.
- Pass a list of all "None" values to ensure the function returns 0 and does not divide by zero.
- Pass a mix of numeric values and "None" values to ensure the average is calculated correctly.
- Pass non-numeric values (e.g., "abc") to confirm whether an exception is expected or should be handled.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- The original code does not safely handle empty or all-None inputs it can divide by zero.
- It does not fully “safely handle mixed input types”, since float(v) can fail for non-numeric values.

### Rewritten explanation
- This function computes the average of valid measurements by ignoring "None" values. It sums all non-None measurements (converted to float) and divides by the number of valid measurements processed. If there are no valid measurements, it returns 0 to avoid division-by-zero errors.

## 4) Final Judgment
- Decision: Approve / **Request Changes** / Reject
- Justification: The original implementation produces incorrect results by counting None values and can crash due to division by zero.
- Confidence & unknowns: Confidence is high that the fix resolves the correctness and divide-by-zero issues; the main unknown is whether non-numeric values are possible and how strictly they should be handled.
