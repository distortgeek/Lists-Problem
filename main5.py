x = int(input("Enter total number of elements in your list : "))
i = 1
list1 = []
while i <= x:
    y = int(input("Enter element : "))
    list1.append(y)
    i += 1
list1.sort()
print("List", ":", list1)
if x%2 != 0:
    a = x//2
    print("The median of list is : ",list1[a])
else:
    b = list1[x//2]
    c = list1[(x//2)-1]
    e = b+c
    f = e/2
    print("The median of list is : ",f)