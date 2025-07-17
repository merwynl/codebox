'''

Class Methods - Allows operations related to the class itself
                Takes (cls) as the first parameter/argument, which represents the class itself.
                (self) are used for instance methods that refer to any instances/objects from that class.

Instance methods - Best for operations on instances of that class (object/instance)
Static methods — Best for utility functions that do not need access to class data.

'''


class Student:
    # Declaring class variables
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

        # Increment a certain value
        Student.count += 1
        Student.total_gpa += gpa

    # Instance Method
    def get_info(self):
        return f"{self.name} {self.gpa}"

    # Class Method
    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}" # Getting access to the class variables

    @classmethod
    def get_average(cls):
        if cls.count == 0:
            return 0
        else:
                # Return the results of incoming class variables.
                return f'Average GPA is = {cls.total_gpa / cls.count:.2f}'

# Creating objects/instance from a class.
# Because we are invoking the Student class, the parameters will be passed into the class variable.
student1 = Student("Ken", 4.5)
student2 = Student("Sara", 3.5)
student3 = Student("Adam", 3)

# Invoking a class method. This has access to the get_count method, which inherits data from the class itself.
print(Student.get_count())

# Invoking another class method
print(Student.get_average())