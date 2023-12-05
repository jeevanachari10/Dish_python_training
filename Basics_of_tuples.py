#----------------Tuples-----------------
mytuple = ("apple", "ball", "cat")
print(mytuple)

#allow duplicates
mytuple = ("apple", "ball", "cat", "apple")
print(mytuple)

#using len()
print(len(mytuple))

#can have different data types
mytuple = (1, 2, 3, "apple", "ball", "cat", True, "apple")
print(mytuple)

#type()
#<class 'tuple'>
print(type(mytuple))

#Accessing tuple items
#using index
print(mytuple[1])

#-ve index
print(mytuple[-1])

#range of indexes
print(mytuple[2:5])
print(mytuple[:4])
print(mytuple[3:])
#same works for -ve indexes as well

#change tuple values
#tuples are immutable as a work around we convert it to list and change the list and convert list back as tuple
thistuple = list(mytuple)
thistuple[-1] = "Dog"
mytuple = tuple(thistuple)
print(mytuple)

#looping through tuple
for i in mytuple:
	print(i)

#using range() and len()
for i in range(len(mytuple)):
	print(mytuple[i])
