# ======================================================================================
# ========================= Slice and join strings =====================================
# ======================================================================================

# Slicing string - extract a subset of the original string (indexing a string).
# Joining string - linking two or more strings together to create a bigger string.

# Example 1: slicing a string

string1 = "Hello, Darling"
print(string1[0])
print(string1[4:7])
print(string1[11:])
print(string1[:5])
print(string1[-11:])
print(string1[60:]) # prints " "
print(string1[:: -1]) # prints the message backwords

# Example 2: joining strings

print("Hello" + " " + "World") # it will print Hello World

greetings = ["Hello", "World"]
print("".join(greetings)) # prints Hello World

name = Todor
print("Hello, " + name + "!") # prints Hello, Todor!

