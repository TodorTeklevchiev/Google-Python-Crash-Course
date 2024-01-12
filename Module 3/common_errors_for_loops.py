# ==============================================================================
# ===================== Commong errors in for loops ============================
# ==============================================================================

# Example 1:

for x in range(25):
    print(x)
#this is the correct way
    
def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)
greet_friends(["Taylor", "Barry", "Johnny", "Lora"])

