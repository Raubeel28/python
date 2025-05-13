from abc import ABC,abstractmethod

class shape:
    @abstractmethod
    def area():
        pass



class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2

class square():
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side**2
    
class triangle:
    def __init__(self,base,hieght):
        self.base=base
        self.hieght=hieght
    def area(self):
        return self.base*self.hieght*0.5
    
class pizza(circle):
    def __init__(self,topping,radius):
        super().__init__(radius)

        self.topping=topping
        


shapes=[circle(4),square(5),triangle(6,7),pizza("pepperroni",15)]
for shape in shapes: 
    print(shape.area())