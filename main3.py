#shopping cart
foods = []
prices = []
total =0

while True:
    food = input("Enter a food you want to buy  (Enter q to exit)")
    if food.lower()== "q":
        break
    else:
        price = float(input("Enter the price of the food :$"))
        foods.append(food)
        prices.append(price)

print ("-----Your Cart-----")
for food in foods:
    print(food,end=" ")
for price in prices:
    total +=price
print()
print (f"Your total is {total}")
