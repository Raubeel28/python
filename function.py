def happy_birthday(name,age):
    print(f"How birthday {name}")
    print(f"You are {age} years old now")
    print("Hip Hip Hip Hurray!!!")

happy_birthday("bro",19)

def add(x,y):
    z = x+y
    return z
print(add(2,8))  

def name(last,first):
    hello =last.capitalize() + " " +first.capitalize()
    return hello
print(name("bro", "code"))