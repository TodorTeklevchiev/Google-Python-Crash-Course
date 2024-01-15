# =======================================================================
# =============== List Comprehensions in Python =========================
# =======================================================================


# Example 1:
multiples = []
for x in range(1, 11):
    multiples.append(x*7)
print(multiples)

# Example 2:
multiples = [x*7 for x in range(1,11)]
print(multiples)

# Example 3:
languages = ['Python', 'Ruby', 'C++', 'C#', 'Java', 'GO']
lengths = [len(language) for language in languages]
print(lengths)

# Example 4:
z = [x for x in range(0,101) if x % 3 == 0]
print(z)