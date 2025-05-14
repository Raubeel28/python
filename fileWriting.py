#python writing file(.txt,.json,.csv)

#1.writing text files---------

#employees=["Eugene","Squidward","Spongebob","Patrick"]

#textdata="I like pizza"
#File_path= "C:/Users/USER/Desktop/Output.txt"
#try:
  #  with open(File_path,"a") as file:
    #    file.write("\n" + textdata)
    #    print(f"txt file {File_path} has been created")
#except FileExistsError:
   # print("file already exxist")
#try:
   # with open(File_path,"w") as file:
      #  for employee in employees:
        #    file.write(employee + "\n")
         #   print(f"txt {File_path } has been created")
#except FileExistsError:
  #  print("File already exist")


#2.Writing json file------------
#import json

#employee={"name":"Spongebob",
   #       "age":30,
  #        "position":"cook"}
#filepath="C:/Users/USER/Desktop/Output.json"

#try:
#    with open(filepath,"w") as file:
 #       json.dump(employee,file,indent=4)
 #       print(f"json file {filepath} has been created")
#except FileExistsError:
#    print("File already exist")

#Creating csv file
#create a 2d list(meaning a list within a list)
import csv
employees=[["Name","Age","Job"],
           ["Spongebob","23","Farmer"],
           ["Patrick",36,"Manager"],
           ["Sandy",35,"Scientist"]]
filepath="C:/Users/USER/Desktop/output.csv"
with open(filepath,"w") as file:
    writer=csv.writer(file)
    for row in employees:
        writer.writerow(row)
    print(f"csv file {filepath} has been created")
