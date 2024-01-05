# =====================================================================================
# ======================= Branching with If statements ================================
# =====================================================================================

# Branching - The ability of a program to alter its execution sequence.

# Example:
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long.")

# The body of the if block will only execute when the condition evaluates to true;
# otherwise it's skipped.
