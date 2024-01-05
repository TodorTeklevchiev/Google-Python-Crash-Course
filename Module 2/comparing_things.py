# ---------------------------------------------------------------------------
# ------------------- Comparing things in Python ----------------------------
# ---------------------------------------------------------------------------

print(10>1) # Boolean - one of two possible states: either true or false >>> True

# Equality operator
print("cat" == "dog") # We use this operator to see if things are equal. >>> False

# Not equals operator !=
print(1 != 2) # It shows us if the operands are not equal. >>> True

# Python doesn't know if a number is smaller/greater than a string.

print(1 == "1") # They are the same. >>> True

# Logical operators in Python - and, or, not. 

# To evalute as true, the and operator would need both expressions to be true at the same time.
print("Yellow" > "Cyan" and "Brown" > "Magenta") # >>> False

# If we use the or operator, instead, the expression will be true if either of ther expressions
# is true, and false only when both expressions are false.
print(25 > 50 or 1 != 2) # >>> True

# The not operator inverts the value of the expression that's in front of it.
print(not 42 == "Answer") # >>> True
print(not 2 == 2) # >>> False


