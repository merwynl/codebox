"""
Variables = a container for a value of piece of data that changes (string, integer, float, boolean)
            a variable behaves as if it was the value it contains.
They are mutable, meaning they can be changed and altered.
Variables can be used to store data in memory to be accessed later.
They should be
    — Descriptive & meaningful
    — Lowercase, separated by underscores
    — UPPERCASE if an item in constant, such as a path
    — Equal sign separated by a space" ="

変数は、さまざまな種類のデータを格納する容器です。
それに、変更可能であり、変更される可能性があることを意味します。
そしたら、データをメモリに保存し、後からアクセスするために使用することができます。
"""

example_integer = 1
example_float = 1.5
example_boole = False
example_string = "Midnight"

number_of_visitors = 5
rating = 7.5
is_released = False
song_name = "白夜"

#  Printing statements
print("好きな曲が 'Secret Trip' という名前です！")
print("めちゃいい曲です！")

''' Comments '''
# This is a comment

''' This is a doc-string '''

# Strings — A string of alphanumeric characters
first_name = "Test"
last_name = "Code"
food = "Okonomiyaki"
email = "fakemail@mail.com"

# Printing & concatenating string variables
print(first_name + " " + last_name)

# String formatting or f-string
print(f"Hello {first_name}.")
print(f"I see you like {food}.")
print(f"Your email is: {email}.")

# Integers — Whole numbers
age = 25
quantity = 5
num_of_students = 30

print(f"You are {age} years old.")
print(f"You are buying {quantity} items.")
print(f"Your class has {num_of_students} students.")

# Float - Decimal numbers
price = 10.99
gpa = 4.5
distance = 2.5

print(f"This Okonomiyaki costs {10.99} yen.")
print(f"My GPA is {gpa}")
print(f"Our destination is roughly {distance}km's away.")

# Boolean — True or false
is_student = True
for_sale = False
is_online = False

print(f"Are you a student?: {is_student}")

# If statements — If something occurs, do something, else do something else.
if is_student:
    print("You are a student")
else:
    print("You are not a student")

if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")

if is_online:
    print("I am currently online")
else:
    print("I am currently AFK")

# Typecasting — Converting one variable type to another
#               str(), int(), float(), bool()

name = "Test Code"
age= 30
gpa = 4.5
is_student = True

# Getting the data type of a variable
print(type(name))

# Swapping variables
x = 10
y = 11

print ('x:', x)
print ('y:', y)
x, y = y, x
print ('x:', x)
print ('y:', y)
