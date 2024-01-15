# ==============================================================
# ==== More string Methods in Python  ==========================
# ==============================================================

"Mountains".upper()
# prints 'MOUNTAINS'

"Mountains".lower()
# prints 'mountains'

# Example 1:
answer = 'YES'
if answer.lower() == 'yes':
    print("User said yes!")

" yes ".strip() 
# removes the surrounding spaces of the string 
# removes whitespaces

" yes ".rstrip() 
# removes the whitespace just on the right side of the string

" yes ".lstrip() 
# removes the whitespace just on the left side of the string

"My name is Todor and I am happy to be a programmer".count("e")
# it shows us how many time a character is found in a string

"Forest".endswith('rest')
# is the string ends with a specific substring, returns boolean

"Forest".isnumeric()
# False

"12345".isnumeric()
# True
# shows us if the string is made just from numbers

" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"])
# methon 'join' concatenate strings

"This is another example".split()
# this is spliting the string into a list of strings




