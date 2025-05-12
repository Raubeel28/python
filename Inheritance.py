class Animal:
    def __init__(self,name):
        self.name=name
        self.isalive=True

    def eat(self):
         print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog =Dog("Scooby")
cat=Cat("grafield")

print(dog.name)
dog.eat()