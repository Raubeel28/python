class Student:
    classyear=2024
    numofstudent=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.numofstudent+=1

student1=Student("spongebob",15)
student2=Student("Patrick",16)

print(student1.name)
print(Student.classyear)
print(Student.numofstudent)