"""
[summary]
"""
#   vars
myInt = 100
string = "foo"
myFloat = 1.25
myBool = True

# Converting a float to an int truncates the decimal value
myFloat = int(myFloat)
print(int(myFloat))

# Converting an int to a float adds a decimal value of .0 at the end.
myInt =  float(myInt)
print(myInt)

# Converting the previous variable from a float to a string should look the same but be aware of type conversion.
myInt = str(myInt)
print(myInt)
print(type(myInt))

# += an int value increments the existing int
age = 100
age += 1  # Same as age ＝ age + 1
print(age)

# += on a str concatenates the value to the existing string
age = str(age)
age += "1"  # Same as age ＝ age + 1
print(age)

# Typecasting a string to a bool will always return True
string = bool(string)
print(string)

# Typecasting an empty string to a bool will always return False
name = ""
name = bool(name)
print(name)