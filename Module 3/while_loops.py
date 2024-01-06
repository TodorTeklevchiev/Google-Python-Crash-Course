# ======================================================================================
# ==================== While Loops in Python ===========================================
# ======================================================================================

"""
while loops - Instruct your computer to continously execute your code based on the value of condition.

initializing - To give an initial value to a variable.

              
"""

# Example 1:

x = 0
while x <5:
    print("not there yet, x =" + str(x))
    x = x + 1 # is the same as [x += 1]
print("x=" + str(x))


# Example 2:

def attempts(n):
    x = 1
    while x <= n:
        print("Attempt" + str(x))
        x += 1
    print("Done")
attempts(5)
