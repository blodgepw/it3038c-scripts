import datetime
try:
    print("How old are you in terms of age, month, and day?\n")
    age = int(input("Enter your age:"))
    month = int(input("Enter your month:"))
    days = int(input("Enter your days:"))

    seconds = 86400 *(age * 365 + month * 30 + days)
    print("You are this old in seconds:", seconds)
except:
    print("Oops, something is wrong!")
