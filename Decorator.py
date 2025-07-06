def addsprinkle(func):
    def wrapper(*args,**kwargs):
        print("You want sprinkles too")
        func(*args,**kwargs)
    return wrapper
def addfudge(func):
    def wrapper(*args,**kwargs):
        print("You add fudge")
        func(*args,**kwargs)
    return wrapper


@addfudge
@addsprinkle
def getice(flavor):
    print(f"Here is your {flavor} icecream🍦")

getice(flavor="Vanilla")
