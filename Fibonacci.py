# write a script to print fibonacci series
num=int(input("enter a number: "))
a=0
b=1
c=0
while c<=num:
 print(c)
 a=b
 b=c
 c=a+b
print(c)
