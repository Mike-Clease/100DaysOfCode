print('Welcome to the tip calculator.')

bill = input("What was the total bill? $")
tip = input("What tip would you like to give, 10, 12 or 15 percent? ")
people = input("How many people are there? ")

#calculate total plus tip
total = float(bill) * int(tip)/10

#calculate what each person owes
per_person = round(total / int(people), 2)

# Print Output
print(f"Each person should pay: ${per_person}")