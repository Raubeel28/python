principal =0
rate =0
time =0

while principal <=0:
  principal = float(input("Enter your principal amount"))
if principal <0:
  print ("principal cannot be less than or equal to zero")

while rate<=0:
  rate=float(input("Enter your rate amount"))
if rate<0:
  print ("rate cannot be less than or equal to zero")

while time <=0:
 time =int(input("Enter your time in years"))
if time <0:
  print ("Interest cannot be less than or equal to zero")

print(principal)
print(rate)
print(time)

total = principal * pow((1 + rate/100),time)
print (f"Your new amount is ${total:.2f}")


#Lets try another method
while True:
  principal = float(input("Enter your principal amount"))
  if principal< 0:
    print ("Principal cannot be less than zero")
  else:
    break
while True:
  rate = float(input("Enter your rate"))
  if principal< 0:
    print ("rate cannot be less than zero")
  else:
    break
  
  while True:
   time = int(input("Enter your time"))
  if timel< 0:
    print ("time cannot be less than zero")
  else:
    break
total2 = principal * pow((1 + rate),time)
print(f"Your total is {total2:.2f}")
  

  

