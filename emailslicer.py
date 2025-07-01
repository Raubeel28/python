def main():
    print("welcone to email slicer")
    print("")

    email=input("Please input a valid email  :")  
    (username,domain)=email.split("@")
    (domain,extension)=domain.split(".")

    print("username: ",username)
    print("domain: ",domain)
    print("extension :" ,extension)
main()