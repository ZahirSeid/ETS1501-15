"""
f-strings
len()
str.encode()
"""

string = "Dr Strange"

print(f"i like the 1st movie of {string} rather than the sequels") # we use this method to incorprate variables in string instead of concatinating 

print(len(string)) # print the lenth of character in the string , if it were list it would return the number of objects in that list

print(string.encode()) #  encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used
