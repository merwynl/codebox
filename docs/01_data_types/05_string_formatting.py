"""
[String formatting]
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

# Format specifier
price1 = 3.14159
price2 = -978.65
price3 = 12.34

# Format string to 3 decimal points
print(f"Price 1 is ${price1:.3f}")
print(f"Price 2 is ${price2:.3f}")
print(f"Price 3 is ${price3:.3f}")

# Format string to 2 decimal points
print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.2f}")

# Format string to 1 decimal points
print(f"Price 1 is ${price1:.1f}")
print(f"Price 2 is ${price2:.1f}")
print(f"Price 3 is ${price3:.1f}")

# Adds to spaces before price value
print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")

# Pads the spaces before price value with 0's
print(f"Price 1 is ${price1:010}")
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:010}")

# Left justify the strings, then add 10 spaces after the value
print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}")

# Right justify the string, then add 10 spaces before the value
print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}")

# Center align the string, then add 5 spaces on either side of the printed value
print(f"Price 1 is ${price1:^10}")
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}")

# Displays any positive values with a plus sign &  any negative values with a - sign
print(f"Price 1 is ${price1:+}")
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}")

# Colon space does the same thing
print(f"Price 1 is ${price1: }")
print(f"Price 2 is ${price2: }")
print(f"Price 3 is ${price3: }")

price1 = 3000.14159
price2 = -97800000.6543
price3 = 1200.3402
# Adds a , to any thousand number value
print(f"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")

# Combining different format specifiers to include a + sign and format the numbers to 2 decimal values
print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")