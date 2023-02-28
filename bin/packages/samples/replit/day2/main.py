# # Gets the data type of an input
# num_char = len(input("What is your name?"))
# print(type(num_char))

# # Converts the individual characters in the array into an integer and adds the two values together
# two_digit_number = input("Type a two digit number: ")
# print(int(two_digit_number[0]) + int(two_digit_number[1]))

# # Alternate more readable  approach to the above
# two_digit_number = input("Type a two digit number: ")

# # Get the individual digits
# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[0])

# # Adds the trwo digits together & prints it
# two_digit_number = first_digit + second_digit
# print(two_digit_number)

# # Gets the user's height & weight
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")

# # Calculates the body mass index by dividing the user's weight (in kg) by the square of their height (in m) and prints the result
# height = float(height)
# weight = float(weight)
# bmi = weight / (height ** 2)
# print(round(bmi))

# # f-strings
# score = 0
# height = 1.8
# isWinning = True
# print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

# # Get number of years left
# years_left = 90 - int(age)

# # Get number of days, weeks & months left
# days = round(years_left * 365)
# weeks = round(years_left * 52)
# months = round(years_left * 12)

# # Format & print the total number of days, weeks and months left
# time_left = f"You have {days} days, {weeks} weeks, and {months} months left."
# print(time_left)

age = 12
print(f"You are " + age + " years old")