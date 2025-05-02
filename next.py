rows = int(input("Enter the no_ of rows"))
columns= int( input("Enter the no_ of columns"))
symbol= input("Pls Enter a symbol")

for x in range (rows): 
    for y in range(columns): 
        print(symbol, end="")
    print()