# ===========================================================================
# =============== Modifying contents of a list in python ====================
# ===========================================================================

# Lists are mutable.


# Example 1:
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")
print(fruits)

# Example 2:
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
print(fruits)

# Example 3:
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0,"Orange")
fruits.insert(25,"Peach")
fruits.remove("Banana")
print(fruits)

# Example 4: 
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
# fruits.remove("Pear")
print(fruits)
#this will throw an error

# Example 5:
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0,"Orange")
fruits.insert(25,"Peach")
fruits.remove("Banana")
fruits.pop(3)
print(fruits)

# Example 6:
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0,"Orange")
fruits.insert(25,"Peach")
fruits.remove("Banana")
fruits.pop(3)
fruits[2] = "Strawberry"
print(fruits)