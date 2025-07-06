#filepath="C:\\Users\\USER\\Desktop\\Output.txt"
#try:
  #  with open(filepath,"r") as file:
   #     content=file.read()
   #     print(content)
#except FileNotFoundError:
  #  print("This is not found")
#except PermissionError:
  #  print("You do not have permission to read this file")
#import json
#filepath="C:\\Users\\USER\\Desktop\\Output.json"
#with open(filepath,"r") as file:
 #   content= json.load(file)
 #   print(content)

import csv
filepath="C:\\Users\\USER\\Desktop\\Output.csv"
with open(filepath,"r") as file:
    content=csv.reader(file)
    for row in content:
        print(row)
