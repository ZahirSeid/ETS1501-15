string = "Greeting"

# let's make a variable that has a bunch of characters and lets leave space at the beginning and the end to demonstrate the functionality of .strip() method
sentence = " The new model car is very fast  "

# string_properties 

print(string.count('e')) # this method counts the number of characters in a string , it can be 1 character or multiple

print(string.replace('t', 'g')) # this method allows us to replace a character or multiple chars in a string in this case we are repllacing 't' with 'g'

print(sentence.strip()) # this method allows us to remove whitespace at beginning and at the end; but not in the middle or b/n the chars

print(sentence) # i will print the original one for you to spot the difference



"""
# Output 


2
Greeging
The new model car is very fast
 The new model car is very fast

""" 

# notice when we printed the 'sentence' variable it was printed with whitespace ;  run it to understand and visualize it.

