"""
[summary]
"""

# String formatting or f-string
first_name = "Codebox"
food = "Okonomiyaki"
email = "fakemail@mail.com"

print(f"Hello {first_name}.")
print(f"I see you like {food}.")
print(f"Your email is: {email}.")

# Concatenating f-strings
phrase = "神様になった日"
feeling =  "がかっこいい"
full = f"{phrase}{feeling}"
print(full)

# Example 1
date = 4
month = 2
year = 2025
print (f"Today is {year}年{month}月{date}日")

# Example 2
day_of_week = "月曜日"
print (f"今日は{day_of_week}")

# Example 3
age = 25
quantity = 5
num_of_students = 30
print(f"You are {age} years old.")
print(f"You are buying {quantity} items.")
print(f"Your class has {num_of_students} students.")

# Example 4
is_student = True
print(f"Are you a student?: {is_student}")
