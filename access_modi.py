# By default, all members within a class are public
class ClassScheduledf:
   def __init__(self, course, instructor):
       self.course = course
       self.instructor = instructor
 
   def display_course(self):
       print(f'Course: {self.course}, Instructor: {self.instructor}')

sched = ClassScheduledf('Physics', 'Mr. Mi') # initializing
 
sched.display_course() # prints Course: Physics, Instructor: Mr. Mi
sched.course # prints 'Physics


# Protected access modifiers, denoted with the prefix _, 
# prevent members from being accessed outside of the class, unless it’s from a subclass.
from re import L


class ClassSchedule:
   def __init__(self, course, instructor):
       self._course = course # protected
       self._instructor = instructor # protected
 
   def display_course(self):
       print(f'Course: {self._course}, Instructor: {self._instructor}')
 
sched = ClassSchedule('Physics', 'Miss. Ch')
sched.display_course()


# Private access modifiers, denoted with the prefix __, 
# declare members to be accessible within the class only.
class ClassShedule:
    def __init__(self, course, instructor):
        self.__course = course # private
        self.__instructor = instructor # private

    def display_course(self):
       print(f'Course: {self._course}, Instructor: {self._instructor}')

sched = ClassShedule('Maths', 'Mr. A') 

sched.__course # this will throw an Attribute Error because we're trying to access a private member
 
sched.display_course() # this won't throw an Attribute Error because this method is public