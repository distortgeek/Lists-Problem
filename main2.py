x = int(input("Enter total number of elements in your list : "))
i = 1
list1 = []
list2 = []
list3 = []
list4 = []
while i <= x:
    y = int(input("Enter element : "))
    list1.append(y)
    i += 1
for a in list1:
    if a < 0:
        list2.append(a)
    elif a > 0:
        list3.append(a)
    else:
        list4.append(a)
list1.sort()
print("Original List",":",list1)
list2.sort()
print("List of negative integers",":",list2)
list3.sort()
print("List of positive integers",":",list3)
print("List of zeroes",":",list4)
