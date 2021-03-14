## Import scipy in order to perform more extreme calculations
from scipy import special


## Prompt user with initial calculations
try:
    operation = input("What operation would you like to use (+,-,*,/,exp,cos,sin): ")
    first_number = int(input("What is your first number? "))
    second_number = int(input("What is your second number? "))
## Run the calculations based on the users input
    if operation == "+":
        print(first_number + second_number)
    if operation == "-":
        print(first_number - second_number)
    if operation == "*":
        print(first_number * second_number)
    if operation == "/":
        print(first_number / second_number)
    if operation == "exp": 
        print(special.exp10(first_number))
    if operation == "cos":
        print(special.cosdg(first_number))
    if operation == "sin":
        print(special.sindg(first_number))    
## If user enters incorrectly, display this error
except:
    print("Oh no, something went wrong. Make sure to enter integers or the correct abbreviation.")