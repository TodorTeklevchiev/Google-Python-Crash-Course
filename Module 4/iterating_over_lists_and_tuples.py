# ==========================================================
# ========= Iterating over lists and tuples ================
# ==========================================================

# Example 1:
animals = ["Lists", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)
print("Total characters: {}, Average length: {}".format(chars,chars/len(animals)))

# Example 2:
winners = ["Ashley", "Dylan", "Thomas"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))

# Example 3:
def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name,email))
    return result
print(full_emails([("alex.ivanov@gmail.com", "Alex Ivanov"), 
                   ("todor.teklevchiev@gmail.com", "Todor Teklevchiev")]))