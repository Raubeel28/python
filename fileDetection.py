import os
file_path="C:/Users/USER/Desktop/test"

if os.path.exists(file_path):
    print(f"This location {file_path} exist")

    if os.path.isfile(file_path):
        print(f"This {file_path} is a file")
    elif os.path.isdir(file_path):
        print("This is a folder")
        
    
else:
    print("That file does not exist")



