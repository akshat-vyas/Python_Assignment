# global variable
#local variable is given more reference than global variable
count=9
def plus():
 global count
 count+=1
def minus():
 global count
 count-=1
print("count=",count)
plus()
plus()
minus()
minus()
print("count=",count)
