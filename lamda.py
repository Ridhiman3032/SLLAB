from functools import reduce

n = int(input("Enter number of elemnts in list: "))
myList = []
for i in range(n):
    ele = int(input("Enter list element " + str(i+1)))
    myList.append(ele)

print("Original list is: ")
print(myList)

newList = [(lambda x: 3*x) (x) for x in myList]

print("New list is: ")
print(newList)

print("Sum of elemts of original list: ")
print(reduce(lambda a,b : a+b ,myList))
print("Sum of elemts of new list: ")
print(reduce(lambda a,b : a+b ,newList))
