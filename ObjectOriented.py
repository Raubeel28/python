class Car:
    def __init__(self,model,year,colour,forsale):
        self.model=model
        self.year=year
        self.colour=colour
        self.forsale=forsale
    def drive(self):
        print(f"You drive {self.model}")   
    def describe(self):
        print(f"{self.model},{self.year},{self.colour}")

car1=Car("Mustang",2020,"red",False)
car2=Car("Covert",2020,"blue",False)

car1.drive()
car2.describe()