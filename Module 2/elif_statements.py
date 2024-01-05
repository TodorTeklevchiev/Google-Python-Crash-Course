# ==============================================================================
# ===================== Elif statements in Python ==============================
# ==============================================================================

# Example:
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long.")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long.")
    else:
        print("Valid name.")

"""
Syntax of an if-elif-else block
-------------------------------
    if condition 1:
        action 1
    elif condition 2:
        action 2
    else:
        action 3

"""