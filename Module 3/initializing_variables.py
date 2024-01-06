# ==================================================================================
# =============== Initializing Variables in Python =================================
# ==================================================================================

"""
NameError: name "my_variable" is not define

We need to define the variable before using it in the loop.
Whenever you are writing a loop, check that you are initializing all the variables 
you want to use before you use them.
"""
# Example 1:

my_variable = 5
while my_variable < 10:
    print("Hello!")
    my_variable += 1

# Example 2:

x = 1
sum = 0
while x < 10:
    sum += x
    x += 1

product = 1
x = 1
while x < 10:
    product = product * x
    x += 1
print(sum, product)

# Example 3:

def count_down(start_number):
    current = 7
    while(current > 0):
        print(current)
        current -= 1
    print("Zero!")
count_down(7)