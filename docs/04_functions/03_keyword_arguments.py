"""
Keyword args helps with readibility.
order or args doesn't matter
1. positional
2. DEFAULT
3. keyword
4. arbitrary
"""

# Using kewyword args in function calls to change the order of the parameters. Positional args must come first.
def hello(greeting, title, first, last):
    statement = f"{greeting} {title} {first} {last}"
    return statement
print(hello ("Hello",title="Mr.", last="Smith", first="John" ))

# Using keyword args to print a range of values with a specified step count.
def print_range( max, min = 1 ,step = 1):
    for x in range(min, max, step):
        print(x, end=" ")
    return 0
print_range(21, min=0, step=2)

# Using keyword args to print a phone number
def get_phone(country, area, first, last):
    return f"+{country}-{area}-{first}-{last}"
phone_num = get_phone(country=81,area=80,first=1234,last=5678)
print(phone_num)