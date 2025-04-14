# Create two sets of fruits
basket1 = {"apple", "banana", "cherry", "mango"}
basket2 = {"banana", "kiwi", "mango", "grape"}

# Use 'intersection()' to find common fruits in both baskets
common_fruits = basket1.intersection(basket2)  # this gives us only the fruits found in both sets

print(common_fruits)  # It will show {'banana', 'mango'}

# Use 'difference()' to find fruits only in basket1, not in basket2
unique_to_basket1 = basket1.difference(basket2)  # returns elements in basket1 but NOT in basket2

print(unique_to_basket1)  # It will show {'apple', 'cherry'}

# Use 'symmetric_difference()' to get fruits that are in one basket or the other, but not both
exclusive_fruits = basket1.symmetric_difference(basket2)  # this removes all the common elements

print(exclusive_fruits)  # It will show {'apple', 'cherry', 'kiwi', 'grape'}

# Output

"""
{'banana', 'mango'}
{'apple', 'cherry'}
{'apple', 'cherry', 'kiwi', 'grape'}
"""
