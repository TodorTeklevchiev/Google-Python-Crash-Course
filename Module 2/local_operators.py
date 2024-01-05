# =========================================================================================
# =========================== Local Operators in Python ===================================
# =========================================================================================

'''
AND - Both sides of the statement being evalueated must be True for the whole statement to be True.

OR - If either side of the comparison is True, then the whole statement is true.

NOT - Inverts the Boolean result of the statement immediately following it. So, if a statement evaluates to True,
and we put the not operator in front of it, it would become False.

'''
# ==========================================================================
# PART 1: The AND logical operator:

#Example 1: 
print((6*3 >= 18) and (9+9 <= 36/2))

#Example 2: 
print("Nairobi" < "Milan" and "Nairobi" > "Hanoi")

# ===========================================================================
# PART 2: The OR logical operator:
#Examples:
# True or True returns True
print((15/3 < 2+4) or (0 >= 6-7))
True

# False or True returns True
print("country" == "New York City" or "city" == "New York City")
True

# True or False returns True
print(16 <= 4**2 or 9**(0.5) != 3)
True

# False or False returns False
print("B_name" > "C_name" or "B_name" < "A_name")
False

# ================================================================================
# The NOT logical Operator:

#Example 1:
x = 2*3 > 6
print("The value of x is:")
print(x)

print("")  # Prints a blank line

print("The inverse value of x is:")
print(not x)

#Example 2:
# What happens when you negate a False statement? 
# Click Run when you are ready to check your answer.


today = "Monday"
print(not today == "Tuesday") 


# The "today" variable states today is Monday. This makes the comparison
# "today == Tuesday" False. The logical operator "not" inverts the False
# result to become True. In other words, this expression asks if it is
# false that today is not Tuesday. More succinctly, "not False" means 
# True
