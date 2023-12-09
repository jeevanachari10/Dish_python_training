#Write a python program to get ‘n’ number of items and concatenate to the existing list.
existing_list = [1, 'a', "apple", True]
print(f"existing list:{existing_list}")
mylist = []
n_items = int(input("Enter the number of items you want to add:"))
'''
for i in range(n_items):
  item = input("Enter item:")
  mylist.append(item)
print(mylist)
'''
#above code can be wrote in using comprehension as below
mylist = [input(f"Enter item{i + 1}: ") for i in range(n_items)]

#logic1
existing_list = existing_list + mylist
print(existing_list)

#logic2
del existing_list[-n_items:] #used as clening process for logic1
existing_list.extend(mylist)
print(existing_list)
