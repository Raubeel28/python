import random

def spin_row():
    symbols=["🍉", "🍎", "🍊" ,"🔔" ,"⭐"]
    return [random.choice(symbols) for symbol in range(3)]



def print_row(row):
    print("**********")
    print(" ".join(row))
    print("**********")


def payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[2]=="🍎":
            return bet*3
        elif row[2]=="🍉":
            return bet*2
        elif row[2]=="🍊":
            return bet *4
        elif row[2]=="🔔":
            return bet * 5
        elif row[2]== "⭐":
            return bet * 10
        
    return 0
    

def main():
    balance=100
    print("*************")
    print("Welcome to python Slot")
    print("Symbols:🍉 🍎 🍊 🔔 ⭐")
    print("**************")
    while balance>0:
        print(f"Current balance: {balance}")
        bet = (input("Place your bet:"))
        
        if not bet.isdigit():
            print("Please enter a valid number")
            continue
        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue
        if bet <=0:
            print("Bet must be greater than zero")
            continue
        balance -=bet
        row =spin_row()
        print("Spining......\n")
        print_row(row)
        pay=payout(row,bet)

        if pay>0:
            print(f"You won ${pay}")
        else:
            print("Sorry you lost!!!")
        
        balance +=pay
        play_again = input("Do you want to play again?? (Y/N)").upper()
        if play_again != "Y":
            break

    print("*******************")
    print(f"GAME OVER,your final balance is ${balance}")
    print("*******************")


if __name__== "__main__":
    main ()
