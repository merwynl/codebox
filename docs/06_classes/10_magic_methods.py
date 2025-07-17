'''

Magic Methods - Dunder methods (double underscore) __init__, __str__, __eq__
              - Are automatically called by many of Python's built-in operations
              - Allow developers to define or customise the behaviour of objects.
              - https://www.geeksforgeeks.org/python/dunder-magic-methods-python/

'''

class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"name: {self.name}, gpa: {self.gpa}"

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.gpa > other.gpa


student1 = Student("Ken", 4.5)
student2 = Student("Lisa", 2)

print(student1)
print(student1 == student2)
print(student1 > student2)

class Book:
    # Automatically behind the scene. Incoming parameters are assigned to their respective self. attributes.
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    # Return a string representation of the object
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    # Checks if A is == B
    def __eq__(self, other):
        return self.title == other.title

    # Checks if A > B
    def __gt__(self, other):
        return self.num_pages > other.num_pages

    # Checks if A <>> B
    def __lt__(self, other):
        return self.num_pages < other.num_pages

    # Checks that A is != B
    def __ne__(self, other):
        return self.num_pages < other.num_pages

    # Checks the length of a given attribute
    def __len__(self):
        return len(self.title)

    # Customizing a __add__ dunder method to add two figures together.
    def __add__(self, other):
        return self.num_pages + other.num_pages

    # Checks to see if a certain keyword is found in a given string.
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    # Checks to see if a certain keyword is found in a given string.
    def __getitem__(self, key):
        if key == 'title':
            return self.title
        elif key == 'pages':
            return self.num_pages
        elif key == 'author':
            return self.author
        else:
            return f"{key} was not found."


book1 = Book("ミモザの告白", "八目迷",     342)
book2 = Book("また、同じ夢を見ていた", "住野よる", 264)
book3 = Book("春期限定いちごタルト事件", "米澤穂信", 251)

# Calls the __str__ method to represent an object as a string
print(book1)

# Calls the __eq__ method compared two values. In this case, we're comparing two strings representing the title.
print(book1 == book2)

# Calls the __gt__ method to check if one side is greater than the other.
print(book1 > book3)

# Calls the __lt__ method to check if one side is less than the other.
print(book2 < book3)

# Calls the __ne__ method to check if one side not equal to the other.
print(book2 < book3)

# Calls the __len__ method to check the length of a string.
print(len(book2))

# Calls the __add__ method to add two values together.
print(book2 + book3)

# Calls the __contain__ method to check if a keyword is contained within a given attribute.
print("八目" in book1)

# Calls the __getitem__ method to get the value of a given key
print(book2['audio'])