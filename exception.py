try:
    number=input("Enter a number")
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by Zero you IDIOT")
except TypeError:
    print("Type in only numbers please")
except Exception:
    print("Something went wrong")
finally:
    print("Do some clean up Cleanup here")