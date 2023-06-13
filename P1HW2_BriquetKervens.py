# This program calculates and displays travel expenses

# 06/13/2023

# CTI-110 P1HW2 - Travel Expense

# Briquet Kervens

#

print("This program calculates and displays travel expenses")
print()
budget = int(input("Enter Budget:"))
print()
travel = input("Enter your travel destination:")
print()
gas=int(input("How much do you think you will spend on gas?"))
print()
hotel = int(input("Approximately, how much will you need for accomodation/hotel?"))
print()
food = int(input("Last, how much do you need for food?"))
print("-"*12,"Travel Expenes","-"*12)
print("Location:" + travel)
print("Initial Budget:",budget)
print()
print("Fuel:",gas)
print("Accomodation:",hotel)
print("Food:", food)
print()
print("Remainig Balance:",budget-(gas+hotel+food))

