capitals = {
    "France": "Paris",
    "Japan": "Tokyo",
    "Brazil": "Brasília"
}

# Using items() to get all key-value pairs
print(capitals.items())  # It will show dict_items([('France', 'Paris'), ('Japan', 'Tokyo'), ('Brazil', 'Brasília')])

# Using get() to safely access the value for a key
print(capitals.get("Japan"))  # It will show 'Tokyo' (returns the value for 'Japan')
print(capitals.get("Germany"))  # It will show 'None' since 'Germany' is not in the dictionary

# Using pop() to remove a key and get its value
removed_capital = capitals.pop("Brazil")  # removes 'Brazil' from the dictionary and returns its capital

print(removed_capital)  # It will show 'Brasília'
print(capitals)  # It will show {'France': 'Paris', 'Japan': 'Tokyo'}

# Output

"""
dict_items([('France', 'Paris'), ('Japan', 'Tokyo'), ('Brazil', 'Brasília')])
Tokyo
None
Brasília
{'France': 'Paris', 'Japan': 'Tokyo'}
"""
