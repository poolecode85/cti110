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
print('----------Travel Expenses----------')


print(f'{'Location:':<17}  {'Destination':<10}')
print(f'{'Initial Budget:':<18} ${Budget:<10.2f}')

print(f'{'Fuel:':<18} ${Gas:<10.2f}')

print(f'{'Accomodation:':<18} ${Accomodations:<10.2f}')

print(f'{'Food:':<18} ${Food:<10.2f}')
print('------------------------------------')
print('\n')

print(f'{'Remaining Balance:':<18} ${Budget - Gas - Accomodations - Food:<10.2f}')
