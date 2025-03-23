name = "zahir"

print(f'hello my name is {name}')

age = input("Please insert your age: ")
test = input("please insert a number this one is for a test: ")

print("the type for the test is ") 
print(type(test))

print("I am " + age + " years old.")

age = int(age) # we need to convert it to int before we compare , why? because input passes the number as string and the conditional statment is comparing integers not string
if age >= 21:
    print("You are getting old :)")
elif 18 <= age <= 20:
    print("Time flies by, trust me")
elif age > 30:
    print("Excuse me sir")
else:
    print("you are a child")

# slicing examples

random_strings = "ehellotworld"


word1 = random_strings[1:6]  # "hello"
word2 = random_strings[7:]   # "world"

print(word1)
print(word2)

