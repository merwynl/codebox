
# If statements = Do something IF a condition is True
#                 Else do something else

# # Example 1
# is_student = True
# if is_student:
#     print('学生です')
# else:
#     print('学生じゃない')
#
# # Example 2 — Querying a user input to verify a condition
# age = int(input("Please enter your age: "))
# if age >=18:
#     print("You may purchase this alcoholic beverage.")
# else:
#     print("I'm sorry, you are not of the sufficient age to make this purchase.")
#
# # Example 3 - Querying a user input to verify a condition
# time = int(input("Please enter your desired time slot(in hrs): "))
# if time >= 17:
#     print ("Reserved seating has been sold out. You may purchase tickets for general standing admission tickets.")
# elif time <=0:
#     print("You have entered an invalid number. Please try again.")
# else:
#     print("There are still available reserved seating ")
#
# # Example 4 - Double equal sign is used as a comparison operator to compare two values.
# response = input("お部屋でご掃除をいかがでしょうか？ (はい/いいえ): ")
# if response == "はい":
#     print("かしこまりました！明日11時頃お部屋を掃除いたします。")
# elif response == "いいえ":
#     print("承知いたします！ごゆっくりお過ごしください！")
#
# # Example 5 -
# name = input("お客様のお名前ここで入力してください:　")
# if name == "":
#     print("大変申し訳ございませんです！お客様のお名前がご存在しません。もう一度入お客様の名前をご確認ください。")
# else:
#     print(f"お客様のお名前が確認しました。{name}様、東京ホテルへようこそ。ごゆっくりどうぞ。")
#
# # Example 6 - Using if statements with booleans
# # The value may be omitted from the if statement
# for_sale = True
#
# if for_sale:
#     print ("承知いたします。レジ袋いかがでしょうか？")
# else:
#     print ("大変申し訳ございませんです！この商品は非常品です！")
#
# # Example 7
# smoking_permitted = True
# if for_sale:
#     print("このエリアでの喫煙は許可されていおります。")
# else:
#     print("大変申し訳ございませんです！このエリアが禁煙しております。")

# Simple calculator program
operator = input("Please enter an operator (+ - * / % ** //): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(f"The result of {num1} {operator} {num2}: {round(result, 2)}")
elif operator == "-":
    result = num1 - num2
    print(f"The result of {num1} {operator} {num2}: {round(result, 2)}")
elif operator == "*":
    result =  num1 + num2
    print(f"The result of {num1} {operator} {num2}: {round(result, 2)}")
elif operator == "/":
    result = num1 / num2
    print(f"The result of {num1} {operator} {num2}: {round(result, 2)}")
elif operator == "%":
    result =  num1 % num2
    print(f"The result of {num1} {operator} {num2}: {round(result, 2)}")
elif operator == "**":
    result = num1 ** num2
    print(f"The result of {num1} {operator} {num2}: {round(result, 2)}")
elif operator == "//":
    result =  num1 // num2
    print(f"The result of {num1} {operator} {num2}: {round(result, 2)}")
else:
    print("Incorrect value &/ operator detected. Please assign a valid operator!")