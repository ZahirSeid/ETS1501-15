fruits = ["bananas", "oranges", "dates", "avocados"]

# Append 'apple' to the list
fruits.append('apple')

print(fruits)  # It will show ['bananas', 'oranges', 'dates', 'avocados', 'apple']

# Insert 'grapes' at the second position (index 1)
fruits.insert(1, 'grapes') # so we insert the index at the first argument and the string or int in the 2nd arg

print(fruits)  # It will show ['bananas', 'grapes', 'oranges', 'dates', 'avocados', 'apple']

# Remove 'oranges' from the list
fruits.remove('oranges')

print(fruits)  # It will show ['bananas', 'grapes', 'dates', 'avocados', 'apple']

# Output 

"""
['bananas', 'oranges', 'dates', 'avocados', 'apple']
['bananas', 'grapes', 'oranges', 'dates', 'avocados', 'apple']
['bananas', 'grapes', 'dates', 'avocados', 'apple']

"""
