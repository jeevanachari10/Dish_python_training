#-----------------Lists----------------------
my_list = [1, 2, 3, "apple", "banana", True]
print(my_list)

#duplicate list entries
my_list = [1, 2, 3, "apple", "banana", True, "banana"]
print(my_list)

#list length
print(len(my_list))
print(my_list.count("banana"))

#list type
print(type(my_list))
#<class 'list'>

#Acess items
#print second item using index
print(my_list[1])

#-ve index
print(my_list[-1])

#using range
print(my_list[2:5]
print(my_list[:4]
print(my_list[2:]
#same applies to -ve indexes

#Change list items
#using index
my_list[4] = "kiwi"
print(my_list)


#Add list items
#using append funtion
my_list.append("orange")
print(my_list)

#using insert function
my_list.insert(1, "cherry")
print(my_list)

#using extend funtion
my_list = [1, 2, 3, "apple", "banana", True]
newlist = ["cherry", "kiwi"]
my_list.extend(newlist)
print(my_list)

#Remove list items
#using remove functions
my_list.remove("kiwi")
print(my_list)

#using pop function
my_list.pop(1)
print(my_list)

my_list.pop()
print(my_list)

#using del funtion
del my_list[2]
print(my_list)

#using clear function
my_list.clear()
print(my_list)

#looping in lists
my_list = ["apple", "ball", "cat"]

#basic for loop
for i in my_list:
	print(i)

#using range() and len() function
for i in range(len(my_list)):
	print(my_list[i])

#using list comprehension
[print(i) for i in my_list]

#iterables using list comprehension
newlist = [x for x in range(10)]
print(newlist)

#sorting the list
my_list = ["cat", "ball", "dog", "apple"]
my_list.sort()
print(my_list)
my_list.sort(reverse = True)
print(my_list)

#reversing the list
my_list = ["cat", "ball", "dog", "apple"]
my_list.reverse()
print(my_list)

#Copying the list
newlist = my_list.copy()
print(newlist)

#another way using list()
listnew = list(my_list)
print(listnew)

'''
Methods
---------	
append()	-->	Adds an element at the end of the list
clear()		-->	Removes all the elements from the list
copy()		-->	Returns a copy of the list
count()		-->	Returns the number of elements with the specified value
extend()	-->	Add the elements of a list (or any iterable), to the end of the current list
index()		-->	Returns the index of the first element with the specified value
insert()	-->	Adds an element at the specified position
pop()		  -->	Removes the element at the specified position
remove()	-->	Removes the item with the specified value
reverse()	-->	Reverses the order of the list
sort()		-->	Sorts the list
'''
