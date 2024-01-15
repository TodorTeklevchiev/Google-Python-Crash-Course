# ==================================================================
# ================= Strings in Python ==============================
# ==================================================================

# The parts of a string

name = "Jaylen"
print(name[1])
print(name[0])
print(name[5])
print(name[-1])
print(name[-2])

# Slice - The portion of a string that can contain more than one
# character; also sometimes called a substring.

color = "orange"
print(color[1:4])
print(color[:4])
print(color[4:])

# Creating new strings
message = "A kong string with a silly typo"
new_message = message[0:2] + "l" + message[3:]
print(new_message)

message = "This is a new message"
print(message)
message = "And another one"
print(message)

pets = "Cats & Dogs"
pets.index('&')

# Method - A function associated with a specific class.

print(pets.index("C"))
pets.index("Dogs")
print("Dragons" in pets)
print("Dogs" in pets)

# Email replacement funtion example:

def replace_domain(email, old_domain,new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email
