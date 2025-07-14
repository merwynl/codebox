
"""
Dictionaries are a collection of {key: value} pairs.
Dictionaries can also be stored/read from other more mutable formats like JSON.
Dictionary keys need to be unique.
Dictionaries are non indexable.
Can't contain duplicates
Ordered & mutable.
"""

# Manually creating a dictionary of capital cities
capitals = {"Japan": "Tokyo",
            "China": "Beijing",
            "Russia": "Moscow",
            "South Korea": "Seoul",
            }

# Using dir function to print the available functions for dictionaries
print (dir(capitals))

# Using help function to print a help guide of available functions.
capitals = {"Japan": "Tokyo",
            "China": "Beijing",
            "Russia": "Moscow",
            "South Korea": "Seoul",
            }
print (help(capitals))

# Using an if statement to verify if a key exists:
capitals = {"Japan": "Tokyo",
            "China": "Beijing",
            "Russia": "Moscow",
            "South Korea": "Seoul",
            }
if capitals.get("Australia"):
    print ("That capital exists")
else:
    print ("City not found")

#  Using Update function to add a new key-value pair
capitals = {"Japan": "Tokyo",
            "China": "Beijing",
            "Russia": "Moscow",
            "South Korea": "Seoul",
            }
capitals.update({"Germany": " Berlin"})
print(capitals)

# Using update function to update the value of an existing key
capitals = {"Japan": "Tokyo",
            "China": "Beijing",
            "Russia": "Moscow",
            "South Korea": "Seoul",
            }
capitals.update({"Germany": " Berlin"})
capitals.update({"Japan": " Nara"})
print(capitals)

# Using popitem function to remove the last key element
capitals = {"Japan": "Tokyo",
            "China": "Beijing",
            "Russia": "Moscow",
            "South Korea": "Seoul",
            }
capitals.update({"Germany": " Berlin"})
capitals.popitem()
print(capitals)

# Using pop function to remove a specific key element
capitals = {"Japan": "Tokyo",
            "China": "Beijing",
            "Russia": "Moscow",
            "South Korea": "Seoul",
            }
capitals.update({"Germany": " Berlin"})
capitals.pop("South Korea")
print(capitals)

#  Clears a dictionary
capitals = {"Japan": "Tokyo",
            "China": "Beijing",
            "Russia": "Moscow",
            "South Korea": "Seoul",
            }
print(capitals)
capitals.clear()
print(capitals)

# Get the value of a specified dictionary key. Returns a None value if key not found.
months = {
    'Jan': '一ヶ月',
    'Feb': '二ヶ月',
    'Mar': '三ヶ月',
    'Apr': '四ヶ月',
    'May': '五ヶ月',
    'Jun': '六ヶ月',
    'Jul': '七ヶ月',
    'Aug': '八ヶ月',
    'Sep': '九ヶ月',
    'Oct': '十ヶ月',
    'Nov': '十一ヶ月',
    'Dec': '十二ヶ月'
}
print(months.get("May"))

# Printing a specific dictionary key value
print(months['Mar'])

# A standard dictionary consisting of two keys 
point = {'x': 1, 'y': 2}

#  Using the keys method to get all the keys in a dict.
keys = months.keys()
print (keys)

# Iterating on every key in a dictionary through a loop
month = months.keys()
for month in months:
    print(month)

#  Using the values method to get all the values in a dict.
values = months.values()
print (values)

# Iterating on every value in a dictionary through a loop
values = months.values()
for value in values:
    print(value)

# Return the key-value pair as a list of tuples
items = months.items()
print(items)

# Prints out every key-value pair item
for key,value in months.items():
    print(f"{key}: {value}")

# Using the dict() function to create a dictionary
point = dict(x=1, y=2)
print(point['x'])

# Adding a new dictionary item
point = dict(x=1, y=2)
point['x'] = 10
point['z'] = 50
print (point)

# Using a loop to check if a key exists inside a dictionary
point = dict(x=1, y=2)
point['x'] = 10
point['z'] = 50
if 'a' in point:
    print (point['a'])

# Using the get method to check if a key exists inside a dictionary. 
# Results key value if successful
point = dict(x=1, y=2)
point['x'] = 10
point['z'] = 50
完成 = point.get('z')
print (完成)

# Sets a default value if a key does not exist
point = dict(x=1, y=2)
point['x'] = 10
point['z'] = 50
完成 = point.get('a', 0)
print (完成)

# Deletes a dictionary item
point = dict(x=1, y=2)
point['x'] = 10
point['z'] = 50
del point['x']
print (point)

# Using a for loop to iterate over a dictionary
point = dict(x=1, y=2)
point['x'] = 10
point['z'] = 50
for key in point:
    print(key, point[key])

# Using the items() in a for loop to return a tuple of the dictionary item
point = dict(x=1, y=2)
point['x'] = 10
point['z'] = 50
for item in point.items():
    print(item)

# Unpacking a key & key value item from a dictionary
point = dict(x=1, y=2)
point['x'] = 10
point['z'] = 50
for key, value in point.items():
    print(key, value)

# A simple dict comprehension that creates a dictionary with 5 keys & multiplies each value by 2
values = {x: x * 2 for x in range(5)}
print (values)