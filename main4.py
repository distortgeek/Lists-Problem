x = int(input("Enter total number of elements in your list : "))
i = 1
list1 = []
list2 = []
list3 = []
while i <= x:
    y = int(input("Enter element : "))
    list1.append(y)
    i += 1
list1.sort()
for j in list1:
    if j not in list2:
        list2.append(j)
list2.remove(max(list2))
print("List : ",list1)
for d in list2:
    if d not in list3:
        list3.append(d)
print("Largest second number in list is : " , max(list3))
