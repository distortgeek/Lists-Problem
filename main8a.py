x = int(input("Enter total number of elements in your list : "))
i = 1
list1 = []
while i <= x:
    y = int(input("Enter element : "))
    list1.append(y)
    i += 1
list1.sort()
print("List", ":", list1)
c = input("Want to remove any element? Yes/No : ")
if c in 'YesyyesY':
    z = int(input("Enter the index value of element : "))
    del list1[z]
    print("New list : ",list1)