# ============================================================================
# ============== Nested loops in Python ======================================
# ============================================================================

# Example 1: 
# Domino blocks
for left in range(7):
    for right in range(left, 7):
        print("[" + str(left)+ "|" + str(right) + "]", end=" ")
    print()

# Example 2: 
# Basketball league games
    
teams = ['Bears', 'Pandas', 'Wolves', 'Wild Cats']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)

# Example 3:
