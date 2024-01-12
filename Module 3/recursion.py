# ============================================================================
# ==================== What is recursion =====================================
# ============================================================================

# Recursion - The repeated application of the same procedure to a smaller problem
# Recursion lets us tackle complex problems by reducing the problem to a simpler one.
# In programming recursion is a way of doing a repetitive task by having a function call itself.

# Example 1:

def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1) # recursive case




