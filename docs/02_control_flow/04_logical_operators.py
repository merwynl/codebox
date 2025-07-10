"""
and or not logical operators
evaluates multiple conditions

and = both conditions are true
or = at least one condition is true
not = inverts the condition
"""

# And operator: Checks if all conditions are true
max = 10
min = 5
value = float(input("Enter a number: "))

if value >= min and value <= 10:
    print (f"The value {value} is within the permissible limit")
else:
    print ("The value is outside the bounds")

# Using and operator to verify if a name exists
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

if first_name == "John" and last_name =="Smith":
    print ("Identification verified. Welcome John.")
else:
    print ("ID not verified. Please try again")

# Using logical operators to check for multiple conditions
temp = 25
is_raining = False
is_sunny = True

if temp > 35 or temp < 0 or is_raining:
    print ("本日のイベントが停止さておりましす。大変お詫びいたします。")
else:
    print("本日のイベントが間もなく開催さています。")

if temp >= 28 or is_sunny:
    print ("本日のイベントが停止さておりましす。大変お詫びいたします。")
elif temp <= 0 and is_sunny:
    print("本日のイベントが停止さておりましす。大変お詫びいたします。")
elif temp < 28 and temp > 0 and is_sunny:
    print("本日のイベントが間もなく開催さています。")
elif temp >= 28 or not is_sunny:
    print("本日のイベントが間もなく開催さています。")
elif temp <= 0 and not is_sunny:
    print("本日のイベントが間もなく開催さています。")
elif temp < 28 and temp > 0 and not is_sunny:
    print("本日のイベントが停止さておりましす。大変お詫びいたします。")
else:
    print("本日のイベントが間もなく開催さています。")

    
