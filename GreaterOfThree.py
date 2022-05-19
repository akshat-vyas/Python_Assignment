#program to find greater from 3 numbers...
a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
if a==b and a>c:
 print(a,"and",b,"are equal and greater than",c)
elif a==b and a<c:
 print(a,"and",b,"are equal and smaller than",c)
elif b==c and b>a:
 print(b,"and",c,"are equal and greater than",a)
elif b==c and b<a:
 print(b,"and",c,"are equal and smaller than",a)
elif a==c and a>b:
 print(a,"and",c,"are equal and greater than",b)
elif a==c and a<b:
 print(a,"and",c,"are equal and smaller than",b)
elif a==b==c:
 print(a,"and",b,"and",c,"are equal")
elif a>b and a>c:
 print(a,"is greater than",b,"and",c)
elif b>c and b>a:
 print(b,"is gretaer than",a,"and",c)
else:
 print(c,"is greater than",a,"and",b)
