class Student:     #Class created
    def __init__(self):
        self.name=input("Enter student name:")
        self.age=input("Enter student age:")     #name and age attributes along with the list
        self.marks=[]                                       # to contain marks for 3 subjects

    def accept(self):#Accepting values through 'accept' function
        for i in range(3):
            self.marks.append(input("Enter subject "+str(i+1)+" marks"))

    def display(self): #Displaying values through 'display' function
        print("Name: "+self.name)
        print("Age: "+self.age)
        print("Three subject marks are:")
        print(self.marks)
#First Object
print("Student 1:")
s=Student()
s.accept()
#Second Object
print("Student 2:")
s1=Student()
s1.accept()
#Print details of object 
print("\nStudeunt 1");s.display()
print("\nStudeunt 2");s1.display()