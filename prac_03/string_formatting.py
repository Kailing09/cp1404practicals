"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting.
(We prefer f-strings in this subject.)
Want to read more about it?
https://docs.python.org/3/library/string.html#formatstrings
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.4


# Formatting currency (grouping with comma, 2 decimal places):
print("My {} would cost ${:,.2f}".format(name, cost))
print(f"My {name} would cost ${cost:,.2f}")

# Aligning columns by using width after the :
# This loop uses enumerate, useful when you want both the index and value
numbers = [1, 19, 123, 456, -25]

for i, number in enumerate(numbers, 1):
    print(f"Number {i} is {number:5}")

# TODO: Use f-string formatting to produce the output:
# 1922 Gibson L-5 CES for about $16,035!
print(f"{year} {name} for about {cost:,.0f}!")

# TODO: Using a for loop with the range function and string formatting,
# produce the following right-aligned output (DO NOT use a list):
for number in range(0,200,50):
    print(f'{number:>4}')
#   0
#  50
# 100
# 150
