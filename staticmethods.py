class employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position
    def get_info(self):
        return f"{self.name}={self.position}"
    
    @staticmethod
    def isvalid(position):
        validpostion=["Cook","rocket scientist","Manager"]
        return position in validpostion



me=employee("Rabeel","Manager")
you=employee("Robert","cook")

print(employee.isvalid("Cook"))
print(me.get_info())
print(you.get_info())
    