# This program calculates and displays travel expenses

# 06/13/2023

# CTI-110 P2HW1 - Travel Expense

# Briquet Kervens

#

print("This program calculates and displays travel expenses")
print()
budget = float(input("Enter Budget:"))
print()
travel = input("Enter your travel destination:")
print()
gas=float(input("How much do you think you will spend on gas?"))
print()
hotel = float(input("Approximately, how much will you need for accomodation/hotel?"))
print()
food = float(input("Last, how much do you need for food?"))
print("-"*12,"Travel Expenes","-"*12)
print("Location:           " + travel)
print("Initial Budget:     $" + str(budget))
print("Fuel:               $" + str(gas))
print("Accommodation:      $" + str(hotel))
print("Food:               $" + str(food))
print()
print("Remaining Balance:  $" + str(budget - (gas + hotel + food)))
