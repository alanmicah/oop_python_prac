class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class User:
  def __init__(self, username, role="Customer"):
    self.username = username
    self.role = role

  def say_user_info(self):
    print("My username is {}".format(self.username))
    print("My role is {}".format(self.role))

# This subclass inherits directly from 2 classes Employee and User -
# and uses attributes and methods from both
class Admin(Employee, User):
  def __init__(self):
    super().__init__()
    # calling the __init__ method from User class passing in arguments
    User.__init__(self, self.id, "Admin")

  def say_id(self):
    super().say_id()
    print("I am an admin.")

# a class inheritting members from its superclass and its super-superclass
class Manager(Admin):
  def say_id(self):
    print("I am in charge")
    super().say_id()

# Dunder (double underscore) Methods
class Meeting:
  def __init__(self):
    self.attendees = []
  
  def __add__(self, employee):
    print("ID {} added.".format(employee.id))
    self.attendees.append(employee)

  # Write your code
  def __len__(self):
    return len(self.attendees)
  
e1 = Employee()
e2 = Employee()
e3 = Admin()
e4 = Manager()
e4.say_id()

e3.say_user_info()

print("_____")
# Polymorphism
# the ability to apply an identical operation onto different types of objects.

meeting = [Employee(), Admin(), Manager()]
for i in meeting:
  i.say_id()

print("_____")
m1 = Meeting()

m1 + e1
m1 + e2
m1 + e3
print(len(m1))