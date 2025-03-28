string_right = "Happiness, dq" # we added unwanted characters at the end 
string_left = "dq, Happiness" # we added unwanted characters at the beginning 
sentence = "An apple a day keeps a doctor away"

print(string_left.lstrip('dq, ')) # this method removes the whitespace and characters from the left side

print(string_right.rstrip(', dq')) # this method removes the chars and whitespace from the right side 

print(sentence.split()) # this method returns a list of strings, basically it splits them for every whitespace 
print("Happiness".split()) # on this line we expereiment if it returns the chars or just the string it self

"""
# Output 

Happiness
Happiness
['An', 'apple', 'a', 'day', 'keeps', 'a', 'doctor', 'away']
['Happiness']

"""


