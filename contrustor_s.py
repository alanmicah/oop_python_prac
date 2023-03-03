# Constructors

# Constructors are special functions that are executed when an object is instantiated.
# In Python, the __init__() function is used as the constructor and is called when creating an object.

# The self parameter in the __init__() method refers to the current instance
# and the instance variable course allows for input to assign a value
"""
class ClassSchedule:
   def __init__(self, course):
       self.course = course

first = ClassSchedule('Chemistry')
print(first.course)
"""

# Destructors

# Destructors are special functions that are called when an object gets deleted. 
# In Python, the __del__() method is commonly used as the destructor and is called when an object is deleted.

# Python’s built-in __del__() method represents the destructor in a class.
class ClassSchedule:
   def __init__(self, course):
       self.course = course
 
   def __del__(self):
       print('You successfully deleted your schedule')

sched = ClassSchedule('Chemistry')
del sched