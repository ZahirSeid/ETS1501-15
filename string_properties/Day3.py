string = "Hello"

# string_properties

print(string.index('e')) # this method is used to show the index of a character or string we have previously seen this kind of functionality with .find() method

# so if you are wondering what is the difference of b/n those two; 
"""
the major difference between find() and index() methods in Python is how they handle cases when the substring is not found. The find() method returns -1 in such cases, while index() method raises a ValueError.

When to use find() and index()?

    Use find() when we need to check if a substring exists and do not want to handle exceptions.
    Use index() when we are sure that the substring exists or we want an exception to be raised if it doesn’t exist. (GeeksforGeeks, 2024)

"""

print(string.startswith('H')) # this method is used to check if a string start with the specific character we defined in the parameteer
# on our case we checked if it really starts with 'H' and it returns with True (boolean value)

# lets see if its case sensetive; output we will be shown at the end or run it yourself to check it
print(string.startswith('h'))


print(string.endswith('i')) # this method does the opposite fo the .startswith() method, it checks what character is at the ned of the string 


# now lets chekc if they work on more than one character
print(string.startswith('He'))

print(string.endswith('lo'))

"""
# output

1
True
False
False
True
True

# note: The outputs are ordered
"""
