# write a script to find divisor of a number
num=int(input("enter a number: "))
print("divisor of number are:")
for i in range(2,int(num/2)+1): # also take(2,num+1)
 if num%i==0:
 print(i)
