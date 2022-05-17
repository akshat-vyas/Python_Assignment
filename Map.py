# map()function
ages=[12,45,63,16,74,65]
def myfunc(x):
 if x<18:
 return False
 else:
 return True
def myfunc1(x):
 return x*x
adults=filter(myfunc,ages)
for x in adults:
 print(x)
squares=map(myfunc1,adults)
for i in squares:
 print(x)
# with lambda function
ages=[12,45,63,16,74,65]
adults=filter(lambda a:a>18,ages)
squares=map(lambda a:a*a,adults)
print(squares)
