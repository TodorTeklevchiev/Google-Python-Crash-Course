# ======================================================================
# =================== For Loops in Python ==============================
# ======================================================================

# For loop - iterates over a sequence of values

# Example 1:

for x in range(5):
    print(x)

"""
1. In Python, and a lot of other programming languages a range of numbers will start
with the value 0 by default.

2. The list of numbers generated will be one less than the given value.

"""

# Example 2:

friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hello," + friend)

# Example 3:

values = [23, 52, 59, 37, 48]
sum = 0
length = 0

for value in values:
    sum += value
    length += 1

print("Total sum:" + str(sum) + " - Average: " + str(sum/length))

"""
Use for loops when there's a sequence of elements that you want to iterate.

"""
# Example 4:

product = 1
for n in range(1,10):
    product = product * n
print(product)

# Example 5:

def to_celsius(x):
    return(x - 32)*5/9
for x in range(0,101,10):
    print(x, to_celsius(x))


