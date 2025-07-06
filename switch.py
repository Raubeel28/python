def week(day):
    match day:
        case 1:
            return"today is Monday"
        case 2:
            return"today is Sunday"
        case _:
            return"this is not a valid day"
        
print(week(76))

def weekend(day):
    match day:
        case "sunday"|"saturday":
            return "It is a weekend"
        case "Monday"|"Tuesday"|"Wednesday"|"Thusrsday"|"Friday":
            return"It is not a weekend"
        case _:
            return"It is not a weekend"
        
print(weekend("sunday"))