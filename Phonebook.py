#PHONE BOOK
class contact:
 def __init__(self):
 self.contact_name=input("enter contact name: ")
 self.phone_no=input("enter phone_no: ")
 def put_data(self):
 file=open('phonebook.txt','a')
 file.write(self.contact_name+" "+self.phone_no+"\n")
 file.close()
 print("data entered successfully:\n")
 def get_data(self):
 file=open('phonebook.txt','r')
 print("the contact of the file are:\n")
 print(file.read())
 file.close()
c1=contact()
c1.put_data()
c1.get_data()
