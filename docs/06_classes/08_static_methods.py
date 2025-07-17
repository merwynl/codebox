'''

Static Methods - A method that belongs to a class rather than any object/instance of that class.
               — Usually used for general utility functions.

Instance methods - Best for operations on instances of that class (object/instance)
Static methods — Best for utility functions that do not need access to class data.

'''

class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    def get_info(self):
        return f"{self.name} = {self.role}"

    # We don't need to rely or create any objects to use a static method.
    @staticmethod
    def is_valid_role(role):
        valid_roles= ["artist", "manager", "producer", "engineer", "developer", "support"]
        return role in valid_roles

# With static methods, we can directly parse in the name of the class followed by the method.
print(Employee.is_valid_role("cook"))

# Calling a static method
print(Employee.is_valid_role("artist"))

# Creating objects/instances, which can then invoke instance methods.
employee1 = Employee("Ken", "Producer")
employee2 = Employee("Adam", "Manager")
employee3 = Employee("Lisa", "Developer")
employee4 = Employee("Rachel", "Artist")

# Using an instance/object to invoke a class method.
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
print(employee4.get_info())