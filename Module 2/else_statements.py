# ================================================================================
# ==================== Else Statements in Python =================================
# ================================================================================

# Example 1:
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long.")
    else:
        print("Valid name.")

# Example 2:
def is_positive(number):
    if number > 0:
        return True
    else:
        return False
    
# Example 3:
def is_even(number):
    if number % 2 == 0: # Modulo % - returns the remainder after the devision of integers.
        return True
    else:
        return False
    
# When a returnt statement is executed, the function exits,
# so that the code that follows doesn't get executed.