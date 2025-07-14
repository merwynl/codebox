
# Compound interest calculator
principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter a principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to 0")

while rate <= 0:
    rate = float(input("Enter a interest rate: "))
    if rate <= 0:
        print("Interest rate can't be less than or equal to 0")

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to 0")

total = principle * pow((1 + rate / 100), time)
print (f"Balance after {time} year/s: ${total: .2f}")



# Compound interest calculator without defining a specific condition
principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter a principle amount: "))
    if principle < 0:
        print("Principle can't be less than 0")
    else:
        break

while True:
    rate = float(input("Enter a interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than 0")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than 0")
    else:
        break


total = principle * pow((1 + rate / 100), time)
print (f"Balance after {time} year/s: ${total: .2f}")
