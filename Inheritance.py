#INHERITANCE
class person:
 def __init__(self,fname,lname,age):
 self.fname=fname
 self.lname=lname
 self.age=age
 def show(self):
 print(self.fname)
 print(self.lname)
 print(self.age)
class student(person):
 pass
s1=student("Akshat" ,"Vyas", 20)
s1.show()
