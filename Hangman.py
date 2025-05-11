import random

words=( "apple","orange","pineapple","coconut")
# dictionary of key: ()
art = {0:("",
          "",
          "",),
       1:("  O",
          "",
          ""),
       2:("O",
          "|",
          ""),
       3:(" O",
          "/|",
          ""),
       4:(" O",
          "/|\\",
          ""),
       5:(" O",
          "/|\\",
          "/"),
       6:(" O",
          "/|\\",
          "/ \\")}

def display_man(wguesses):
    for line in art[wguesses]:
        print(line)
def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer =random.choice(words)
    hint =["_"]*len(answer)
    wguesses=0
    guessletters=set()
    running=True
    while running:
        display_man(wguesses)
        display_hint(hint)
        guess=input("Enter a letter: ").lower()
        
        if guess in answer: 
            for i in  range (len(answer)):
                if answer[i] ==guess:
                    hint[i]=guess
if __name__=="__main__":
    main()
