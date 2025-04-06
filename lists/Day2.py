fruits = ["bananas", "oranges", "dates", "avocados"]

# pop(): Removes the element at the given position in the list, or
# the last element if no index is specified.
fruits.pop()  # Removes the last item ('avocados')

print(fruits)  # It will show ['bananas', 'oranges', 'dates']

# len(): Returns the length of the list.
length_of_fruits = len(fruits)  # Returns 3 since there are 3 items left

print(length_of_fruits)  # It will show 3

# sort(): Sorts the list in ascending order.
fruits.sort()  # This will sort the list alphabetically

print(fruits)  # It will show ['bananas', 'dates', 'oranges']

# Slicing: Accessing sub-parts of a list.
# For example, accessing the first two items (index 0 and 1)
sliced_fruits = fruits[0:2]  # Gets items from index 0 to 1

print(sliced_fruits)  # It will show ['bananas', 'dates']

# Output

"""
['bananas', 'oranges', 'dates']
3
['bananas', 'dates', 'oranges']
['bananas', 'dates']
"""

