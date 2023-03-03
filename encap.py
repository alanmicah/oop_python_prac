# In object-oriented programming (OOP), encapsulation is a fundamental concept -
# that describes wrapping variables and methods in one unit.
# A class is a popular example of encapsulation

# Class variables
# A class can contain variables that can only be accessed by an object of the class. 
class UserInfo:
   def __init__(self, username, email_address):
       self.username = username
       self.email_address = email_address
user = UserInfo('user123', 'abc@edf.ghi')

# Data can be accessed using variables 
print(user.username)
print(user.email_address)

# Class Methods
# Contains methods that can be accessed by the objects of the class.
class UserInfo:
   def __init__(self, username, email_address):
      self.username = username
      self.email_address = email_address
 
   def check_username(self, username_to_check):
       if username_to_check == self.username:
           return True
       else:
           return False

user = UserInfo('user123', 'abc@edf.ghi')
 
print(user.check_username('user123')) # returns True
print(user.check_username('user456')) # returns False 