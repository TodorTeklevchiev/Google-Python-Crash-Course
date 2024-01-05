# =======================================================================
# ================== Object-Oriented Programming ========================
# =======================================================================

# OOP - A way of thinking about and implementing our code.

# 1.Methods - Functions that operate on the attributes of a specifix 
# instance of class.

# Example 1:
class Piglet:
    name = "piglet"
    def speak(self):
        print("Oink! I'm {}! Oink!".format(self.name))
hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()

"""
Variables that have different values for different instances of the same
class are called instance variables.
"""

# Example 2:
class Dog:
    years = 0
    def dog_years(self):
        return self.years * 7
pug = Dog()
print(pug.dog_years())
pug.years = 6
print(pug.dog_years())