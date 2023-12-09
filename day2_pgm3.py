#Create 5 lists. Each list has different objects. Combine first element of all list in one list, second element’s in another list and so on.
list1 = [1, 2, 3, 4, 5]
list2 = [6.1, 7.2, 8.3, 9.4, 10.5]
list3 = ["apple", "banana", "cherry", "kiwi", "orange"]
list4 = ['a', 'b', 'c', 'd', 'e']
list5 = [True, False, True, False, True]

#Logic1
mainlist = []
maxlength = max(len(list1), len(list2), len(list3), len(list4), len(list5))
for i in range(maxlength):
    mainlist.append([])
    if i < len(list1):
        mainlist[i].append(list1[i])
    if i < len(list2):
        mainlist[i].append(list2[i])
    if i < len(list3):
        mainlist[i].append(list3[i])
    if i < len(list4):
        mainlist[i].append(list4[i])
    if i < len(list5):
        mainlist[i].append(list5[i])

for i, j in enumerate(mainlist, start=1):
    print(f"newlist{i}: {j}")

#Logic2
#we can achive this through inbuilt zip function
print()
combindlist = list(zip(list1, list2, list3, list4, list5))
resultlist = [list(item) for item in combindlist] #zip function outputs tuple
for i, j in enumerate(resultlist, start=1):
    print(f"newlist{i}: {j}")
