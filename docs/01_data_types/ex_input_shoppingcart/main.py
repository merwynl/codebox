import math

# Exercise Shopping Cart Program
item = input("Please enter an item: ")
price = float(input("Please enter the current price: "))
quantity = int(input("Please enter the quantity of that item: "))
total = math.ceil(price * quantity)
print(f"You have purchased {quantity} {item.lower()}'s for {math.ceil(price)}円 each.")
print(f"Your total is: {total}円")