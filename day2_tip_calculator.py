print("Welcome to the tip calculator")
total = float(input("\nWhat was the total bill? "))
people = float(input("\nHow many people to split the bill? "))
split = total/people
tip = float(input("\nWhat percentage tip would you like to add? 10, 12 or 15? "))
if tip == 10:
    pay = split * 1.1
elif tip == 12:
    pay = split * 1.12
elif tip == 15:
    pay = split * 1.15
else:
    print("Error! Please choose between 10, 12 or 15")
    exit(1)
print("Everyone should pay: $" + str(pay))