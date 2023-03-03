# Polymorphism in OOP is the concept of classes sharing methods with the same name.
# This becomes useful when there are objects initiated from different classes -
# that may share similar methods.

# Different classes sharing the some methods of the same name
class Checking():
   def type(self):
       print('You have a checking account at the Codecademy Bank.')
 
   def balance(self):
       print('$20 left in your checking.')
 
class Savings():
   def type(self):
       print('You have a savings account at the Codecademy Bank.')
 
   def balance(self):
       print('$1000 left in your savings.')

# executers the method for each class
account_a = Checking()
account_b = Savings()
 
for account in (account_a, account_b):
   account.type()
   account.balance()


students1 = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
students2 = {'Alice', 'Lily', 'Zhuo', 'Amy', 'Jane'}
students3 = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
students4 = {'Alice', 'Lily', 'Zhuo', 'Amy', 'Jane'}
 
students1.update(students2)
print(students1)
students3.union(students4)
print(students3)