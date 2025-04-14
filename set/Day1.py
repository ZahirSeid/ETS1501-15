# Create a set of vegetables
vegetables = {"carrot", "lettuce", "onion"}

# Add 'tomato' to the set
vegetables.add("tomato")  # 'add()' adds a single element to the set

print(vegetables)  # It will show {'carrot', 'lettuce', 'onion', 'tomato'} (note: sets don't keep order)

# Remove 'lettuce' from the set
vegetables.remove("lettuce")  # 'remove()' deletes the specified element from the set

print(vegetables)  # It will show {'carrot', 'onion', 'tomato'}

# Create another set of more vegetables
more_vegetables = {"spinach", "cucumber", "onion"}

# Use 'union()' to combine both sets (no duplicates)
all_vegetables = vegetables.union(more_vegetables)  # returns a new set with elements from both sets

print(all_vegetables)  # It will show {'carrot', 'onion', 'tomato', 'spinach', 'cucumber'}

# Output

"""
{'carrot', 'lettuce', 'onion', 'tomato'}
{'carrot', 'onion', 'tomato'}
{'carrot', 'onion', 'tomato', 'spinach', 'cucumber'}
"""
