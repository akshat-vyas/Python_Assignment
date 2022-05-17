#write a script to check wheather a string is palindrom or not
txt=input("enter a string: ")
txt1=txt[::-1]
print("original string= ",txt)
print("reverse string= ",txt1)
if txt==txt1:
 print("original string is equal to reverse string")
 print(txt,"is a palindrom string")
else:
 print("original string is not equal to reverse string")
 print(txt,"is not a palindrom string")
