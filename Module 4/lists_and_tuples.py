# =============================================================================
# ===================== Lists and Tuples in Python ============================
# =============================================================================

# Tuples - Sequences of elements of any type, that are immutable.
# The position of the elements inside the tuple have meaning.


# Tuple example:
fullname = ("Todor", "Atanasov", "Teklevchiev")

# Example 1:
def convert_seconds(seconds):
    hours = seconds/3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours,minutes,remaining_seconds
result = convert_seconds(1000)
hours,minutes,seconds = result
print(type(result))
print(result)
print(hours, minutes,seconds)