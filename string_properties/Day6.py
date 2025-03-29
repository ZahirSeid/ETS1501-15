string1 = "Hello"
num = 29  
name = "Zahir"



print(" ".join([string1, name])) # Using join() to combine words with a space in between

print(string1.isalpha())  # This method checks if all characters in the string are alphabetic
print(string1.isdigit())  # This method checks if all characters in the string are digits
# we have to convert them to string type before we use the method on integers since the methods are string methods
print(str(num).isalpha())  
print(str(num).isdigit())  

"""
# Expected Output:
Hello Zahir
True
False
False
True
"""
