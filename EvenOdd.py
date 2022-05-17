# program to find a given number id odd or even....
a=int(input("enter a number:"))
print(type(a))
b=a%2
print(b)
if a==0:
 print("number is zero")
elif a%2==0:
 print("number is even")
else:
 print("number is odd")
