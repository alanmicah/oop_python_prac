# Inheritance is a feature of object-oriented programming (OOP) that -
# enables the transfer of methods and properties of one class to another.
# Inheritance allows for reusability of code as well as extending the capability of new classes.

# Parent class known as the base class, is a class whose methods and properties -
# transfer over to the child class

class Person:
   def __init__(self, name, age):
       self.name = name 
       self.age = age 
 
   def print_info(self):
       print(f'{self.name} is {self.age} years old')

# The child class, also known as the derived class, is the class that inherits methods and properties from the parent class.
# The child class must contain the following:
# - Name of the parent class in the definition of the child class
# - Constructor of the parent class called within the constructor of the child class

class Teacher(Person):
    def __init__(self, name, age, subject):
        self.subject = subject

        Person.__init__(self, name, age)

myPewrson = Person("Miss. abc", 28)
myPewrson.print_info()

myTeacher = Teacher("Dr. Hirani", 49, "Computer Science")
myTeacher.print_info()
print(myTeacher.subject)