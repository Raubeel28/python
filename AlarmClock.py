import time
import datetime
import pygame


def set_alarm(alarmtime):
    print(f"Alarm set for {alarmtime}")
    
def main():
    alarmtime=input("Enter your alarm time")
    set_alarm(alarmtime)
    sound_file="Black-Sherif-Soma-Obi-_.mp3"
    is_running= True
    while is_running:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        

        if current_time==alarmtime:
            print("WAKE UP🛌")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running=False


    
        time.sleep(1)


if __name__=="__main__":
    main()
    

