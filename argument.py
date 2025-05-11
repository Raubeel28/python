def hello(greeting,title,first,last):
    print(f"{greeting},{title},{first},{last}")

hello("Hello",last="Jones",first="Rabeel",title="Mr.")

def phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"

phone_num = phone(country=+1,area=876,last=9809,first=957)
print(phone_num)

# ARBITARY ARGUMENTS
def add(*nums):
    total = 0
    for num in nums:
        total +=num
    return total
    
print(add(4,8,987))

def add(*args):
   for arg in args:
       print(arg,end=" ")

add("hello bro code","How are you doing")
print()

# Kwargs 
def address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

address(steet="Kumasi2",city="Kumasi",state="Ashanti")

# Creating a shipping label
def shipping(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    for value in kwargs.values():
        print(value,end=" ")
    print()
    print(f"{kwargs.get('street')}",end=" ")
shipping("Dr.","spongebob","Squarepants",
         street="123",city="Michigan",zip="464")
