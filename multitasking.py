import threading
import time

def walk_dog(firstname,lastname):
    time.sleep(8)
    print(f"You finish walking {firstname}{lastname}")

def take_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(3)
    print("You get the mail")


chore1=threading.Thread(target=walk_dog,args=("scooby","Doo"))
chore1.start()

chore2=threading.Thread(target=take_trash)
chore2.start()

chore3=threading.Thread(target=get_mail)
chore3.start()


chore1.join()
chore2.join()
chore3.join()


print("All chores are complete")