#Traditional loops
doubles=[]
for x in range(1,11):
    doubles.append(x*2)
print(doubles)
double=[x*3 for x in range(1,11)]
print(double)

fruits=["apple","orange","coconut"]
fruits=[fruit.upper() for fruit in fruits]
print(fruits)

fruitchars =[fruit[0] for fruit in fruits]
print(fruitchars)

numbers =[1,-2,3,-4,5,-6]
positive =[num for num in numbers if num>=0]
negative =[num for num in numbers if num<=0]
even =[num for num in numbers if num%2 ==0]
print(positive)
print(even)
print(negative)
grades =[85,42,79,90,56,613,0]
passing_grades =[grade for  grade in grades if grade>=60]
print(*passing_grades)
