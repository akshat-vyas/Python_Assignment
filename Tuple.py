# TUPLE
tuple=(1,2,3,"ram",2.6,"riya","akshat")
print(tuple)
#traversing a tuple
tuple=(1,2,3,"ram",2.6,"riya","akshat")
for i in tuple:
 print(i)
#joining tuple
tuple1=(1,2,3,"ram",2.6,"riya","akshat")
tuple2=(34,56,87,"john")
tuple3=tuple1+tuple2
print(tuple3)
# repeating and replicating tuple
tuple1=(1,2,3,"ram",2.6,"riya","akshat")
tuple2=tuple1*3
print(tuple2)
#slicing the tuple
tuple1=(1,2,3,"ram",2.6,"riya","akshat")
tuple2=tuple1[3:5]
print(tuple2)
tuple3=tuple[0:5:2]
print(tuple3)
# length of tuple
tuple1=(1,2,3,"ram",2.6,"riya","akshat")
print(len(tuple))
#maximum value of tuple
tuple=(10,34,54,23,78,65)
print(max(tuple))
#minimun value of tuple
tuple=(34,32,67,54,18,8)
print(min(tuple))
#index()
tuple1=(1,2,3,"ram",2.6,"riya","akshat")
print(tuple1.index("ram"))
#count()
tuple1=(1,2,3,"ram",2.6,"riya","akshat",3)
print(tuple1.count(3))
# deleting tuple
tuple1=(1,2,3,"ram",2.6,"riya","akshat")
print(tuple1)
del(tuple1)
print("after deleting tuple:")
print(tuple1)
