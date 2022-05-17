# write a script to find factorial of a number
num=int(input("enter a number to find out factorial: "))
if num<0:
 print("factorial of negative number do not exist")
elif num==0:
 print("factorial of 0 is 1")
else:
 fact=1
 for i in range(1,num+1):
 fact=fact*i
 print("the factorial of",num,"is: ",fact)
