menu={"pizza": 3.00,
       "nachos": 4.00,
       "popcorn": 5.00,
       "fries": 6.00,
       "lemonade": 7.00}
cart =[]
total =0
print("-----MENU-----")
for key,value in menu.items():
    print(f"{key:10}:${value:.2f}")
print("--------------")
while True:
    food = input("Enter the foods you want to buy(press q to quit)").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("-----YOUR TOTAL-----")
for food in cart:
    print(food,end=" ")
    total += menu.get(food)
print()
print(f"YOUR TOTAL IS ${total}")