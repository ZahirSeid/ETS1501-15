string = "New Week"
string1= "abc12"
ws=" "
print(string.isalnum())  # Check if the string contains only alphanumeric characters (no spaces or special characters)

print(string1.isalnum())

print(string.isspace())  # Check if the string consists only of whitespace characters

print(ws.isspace())


print(string.format())  # here it does nothing since there are no placeholders in the string

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

# output

""" 
False
True
False
True
New Week
For only 49.00 dollars!

"""
