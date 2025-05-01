principal=0
time = 0
rate= 0
while principal <=0: 
  principal= float(input ("Enter the principal amount"))
if principal <= 0:
  print ("Principal cannot be a negative")

while rate <=0: 
 rate= float(input ("Enter the rate amount"))
if principal <= 0:
  print ("rate cannot be a negative")
   
while time<=0: 
  time= int(input ("Enter the time amount"))
if principal <= 0:
  print ("time cannot be a negative or zero") 
print (principal)
print (time)
print (rate)
