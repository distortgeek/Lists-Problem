x = int(input("Enter total number of elements in your list : "))
i = 1
list1 = []
while i <= x:
    y = int(input("Enter element : "))
    list1.append(y)
    i += 1
list1.sort()
a = int(input("Enter the element whose count you want to check : "))
print("The element",a,"occurred",list1.count(a),"times.")
print("List",":",list1)
