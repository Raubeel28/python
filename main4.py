fruits = ["apple","pineapple","banana"]
vegtas= ["onion","tomato","lettuce"]
meats = ["mutoon","beef","fish"]
groceries = [fruits,vegtas,meats]

for collection in groceries:
    for food in collection:
        print(food,end=" ")
    print ()

#creating a phone key pad using 2d collection
keypad =((1,2,3),
         (4,5,6),
         (7,8,9),
         ("*",0,"#")) 

for rows in keypad:
    for num in rows:
        print(num,end=" ")
    print()