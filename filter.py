# filter() function
def myfunc(x):
 if x<18:
 return False
 else:
 return True
adults=filter(myfunc,ages)
for x in adults:
 print(x)
# with lambda function
ages=[12,45,63,16,74,65]
adults=filter(lambda a:a>18,ages)
print(adults)
