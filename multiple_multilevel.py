class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} has been sleeping")
    


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Predator,Prey):
    pass

rabbit =Rabbit("Buggs")
hawk=Hawk("Tony")
fish=Fish("Catfish")

rabbit.flee()
fish.flee
rabbit.sleep()
fish.sleep()
fish.hunt()