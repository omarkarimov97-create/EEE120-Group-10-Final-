def check_eligibility(A, B, C, D):
    # Eligible
    eligible = A and B and C and (not D)

    # Conditional (ровно одно условие не выполнено)
    cond1 = (not A) and B and C and (not D)
    cond2 = A and (not B) and C and (not D)
    cond3 = A and B and (not C) and (not D)
    cond4 = A and B and C and D

    conditional = cond1 or cond2 or cond3 or cond4

    # Not Eligible
    not_eligible = not (eligible or conditional)

    return eligible, conditional, not_eligible


# Test
A = True   # Attendance
B = True   # Assignments
C = True   # Fees
D = False  # Warning

e, c, n = check_eligibility(A, B, C, D)

print("Eligible:", e)
print("Conditional:", c)
print("Not Eligible:", n)