# reduce() function
from functools import reduce
def myfunc(a,b):
 return a+b
val=[1,2,3,4,5]
add=reduce(myfunc,val)
print("addition=",add)
# with lambda function
from functools import reduce
val=[1,2,3,4,5]
add=reduce(lambda a,b:a+b,val)
print("addition=",add)
