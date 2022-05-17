# DICTIONARY
#creating dictionary
dict={"brand":"suzuki","model":"dzire","year":2002,"color":"white"}
print(dict)
# accessing items
dict={"brand":"suzuki","model":"dzire","year":2002,"color":"white"}
print(dict)
x=dict["model"]
print(x)
#loop through a ditionary
dict={"brand":"suzuki","model":"dzire","year":2002,"color":"white"}
for i in dict:
 print(dict[i])
dict={"brand":"suzuki","model":"dzire","year":2002,"color":"white"}
for x,y in dict.items():
 print(x,y)
#change value
dict={"brand":"suzuki","model":"dzire","year":2002,"color":"white"}
dict["year"]=2008
print(dict)
# adding new element
dict={"brand":"suzuki","model":"dzire","year":2002}
print(dict)
dict["color"]="black"
print(dict)
#len()
dict={"brand":"suzuki","model":"dzire","year":2002,"color":"white"}
print(len(dict))
#pop()
dict={"brand":"suzuki","model":"dzire","year":2002,"color":"white"}
print(dict)
dict.pop("model")
print(dict)
#popitems()
dict={"brand":"suzuki","model":"dzire","year":2002,"color":"white"}
print(dict)
dict.popitem()
print(dict)
#del keyword
dict={"brand":"suzuki","model":"dzire","year":2002,"color":"white"}
print(dict)
del dict["year"]
print(dict)
# clear keyword
dict={"brand":"suzuki","model":"dzire","year":2002,"color":"white"}
print(dict)
dict.clear()
print(dict) #ERROR
# copy()
dict={"brand":"suzuki","model":"dzire","year":2002,"color":"white"}
x=dict.copy()
print(x)
# update()
dict={"brand":"suzuki","model":"dzire","year":2002}
dict.update({"color":"white"})
print(dict)
