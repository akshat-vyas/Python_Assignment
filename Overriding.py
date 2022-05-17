# method overriding
class Employee:

 def message(self):
 print('This message is from Employee ')

class Department(Employee):

 def message(self):
 print('This Department inherited from Employee')
class Sales(Employee):

 def message(self):
 print('This Sales is also inherited from Employee')

emp = Employee()
emp.message()

print('------------')
dept = Department()
dept.message()
print('------------')
sl = Sales()
sl.message()
