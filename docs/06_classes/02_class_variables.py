'''

Class variables = shared amongst all instances of a class
                  Defined outside the constructor
                  Allow you to share data among all objects created from that class.

'''


class Student:
    # Self refers to the object we're currently working with. Used to access vars that belong to the class.

    # Declaring a class var. All objects & instances that invoke this class will have access to all these vars.
    class_year = 2024
    num_students = 0

    # Example of a constructor
    # __init__ are always executed when a class is initialised.
    def __init__(self, name, age, class_year=2025, major="English", gpa=4.5, is_on_probation=False):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

        # This will overwrite the class var declared outside the constructor
        self.class_year = class_year

        # Accessing a class variable to modify
        Student.num_students += 1

    # Function for determining the honor roll
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

# Invoking a class object and providing some attributes
student1 = Student("Adam", "20", is_on_probation=True, major="CS")
student2 = Student("Lisa", "23", gpa=4.5, major="Liberal Arts")
student3 = Student("Ken", "21", gpa=5.0, major="Classical History")
student4 = Student("Sara", "25", gpa=4.25, major="Literature")


# Calling and displaying specific class attributes.
print(student1.is_on_probation)
print(student1.gpa)

# Accessing object variables and displaying it
print(student2.name)
print(student2.gpa)

# Accessing a class variable through an object.
# This returns the value of the object var declared within the constructor.
print(student2.class_year)

# Accessing a class variable through the name of the class
# Better to access a class variable through the name of the class rather than an object.
# More explicit and it helps with clarity and readability.
print(Student.class_year)

# Accessing a class variable that has been modified in the constructor.
print(Student.num_students)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students.")
