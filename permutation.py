# permutation
"""n=int(input("enter a total items: "))
r=int(input("enter a number of item to be arrange: "))
# calculate n factorial
fact_n=1
for i in range(1,n+1): #(n,0,-1)
 fact_n*=i
#calculation of (n-r)factorial
x=n-r
fact_x=1
for i in range(1,x+1):
 fact_x*=i
P =fact_n/fact_x
print("P= ",P)"""
# using function
"""def fact(n):
 fact_n=1
 for i in range(1,n+1):
 fact_n*=i
 return(fact_n)
x=int(input("enter total: "))
y=int(input("enter value: "))
fx=fact(x)
fy=fact(x-y)
p=fx/fy
print("P=",p)"""
# find area and circumference of circle
def area(r):
 a=22/7*r*r
 return(a)
def circumference(r):
 pi=3.14
 c=2*3.14*r
 return(c)
r=int(input("enter a radius: "))
a=area(r)
c=circumference(r)
print("area of circle: ",a)
print("circumference of circle: ",c)
