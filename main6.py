x = int(input("Enter total number of elements in your list : "))
i = 1
list1 = []
list2 = []
while i <= x:
    y = int(input("Enter element : "))
    list1.append(y)
    i += 1
list1.sort()
print("Original List", ":", list1)
for j in list1:
    if j not in list2:
        list2.append(j)
print("New List Without any Repetition of Element : ",list2)