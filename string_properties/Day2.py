string = "good"

# string properties 

print(string.capitalize()) # this makes our first letter uppercase

print(string.swapcase()) # this makes our string in opposite case , for examle if it was all lowercase it converts it to all uppercase

print(string.find('d')) # this method is used for finding the index of a letter in a string

"""
# output 

Good
GOOD
3

note: you might wonder what's the d/c b/n title() and capitalize() methods, here is the explanation, "The primary difference between str.capitalize() and str.title() lies in their scope of capitalization. str.capitalize() only capitalizes the first character of the entire string and str.title() capitalizes the first character of every word in the string." (GeeksforGeeks, 2024)

Reference
GeeksforGeeks. (2024, December 30). Difference between str.capitalize() and str.title(). GeeksforGeeks. https://www.geeksforgeeks.org/difference-between-str-capitalize-vs-str-title/
"""
