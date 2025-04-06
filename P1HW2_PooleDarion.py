# Darion Poole
# 04/06/2025
# P1HW2
# Creating code for expenses

print('This program calculates and displays travel expenses')

print('\n')

Budget = int(input('Enter Budget: '))
print('\n')
Destination = (input('Enter your travel destination: '))
print('\n')
Gas = int(input('How much do you think you will spend on gas?: '))
print('\n')
Accomodations = int(input('Approximately, how much will you need for accomodation/hotel? '))
print('\n')
Food = int(input('Last, how much do you need for food? '))
print('\n')
print('-----Travel Expenses-----')
print('\n')
print('Location: ', Destination)
print('Initial Budget: ', Budget)
print('\n')
print('Fuel: ', Gas)
print('Accomodation: ', Accomodations)
print('Food: ', Food)

print('Remaining Balance: ', Budget - Gas - Accomodations - Food)

