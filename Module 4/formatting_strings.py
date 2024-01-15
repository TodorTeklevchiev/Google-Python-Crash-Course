# ========================================================================
# ========= Formatting strings in Python =================================
# ========================================================================

# Example 1:
name = "Manny"
number = len(name) * 3
print("Hello {} ,your lucky number is {}.".format(name,number))

# Example 2:
name = "Manny"
print("Your lucky number is {number},{name}".format(name = name, number = len(name)*3))

# Example 3:
price = 7.5
with_tax = price * 1.09
print(price,with_tax)
print("Base price: ${:.2f}. With tax: ${:.2f}".format(price,with_tax))

# Example 4:
def to_celsius(x):
    return (x-32)*5/9
for x in range(0,101,10):
    print("{:>3} F | {:6.2f} C ".format(x,to_celsius(x)))