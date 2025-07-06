class Students:
    count=0
    totalgpa=0
    
    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        Students.count +=1
        Students.totalgpa +=gpa

     
    #Instance Method
    def getinfo(self):
        return f"{self.name} {self.gpa}"
    #Class Method
    @classmethod
    def getcount(cls):
        return f"The total number of students is {cls.count}"
    @classmethod
    def getaverage(cls):
        if cls.count ==0:
            return 0
        else:
            return f"The average of the students gpa {cls.totalgpa/cls.count:.2f}"
    
    
    
    
me=Students("Spongebob",76)
you=Students("Edward",98)


print(me.getinfo())
print(Students.getcount())
print(Students.getaverage())