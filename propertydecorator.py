class Rectangle:
    def __init__(self,width,height):
        self._width=width
        self._height=height

    @property
    def width(self):
        return f"{self._width:.1f}cm"
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    @width.setter
    def width(self,newwidth):
        if newwidth >0:
            self._width=newwidth
        else:
            print("width must be greater than zero")
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")
          
    



rectangle=Rectangle(8,9)
rectangle.width=7
print(rectangle.width)


