# Darion Poole
# 04/25/25
# P4LAB2
# Use while a loop and for loop together

'''
Get integer from the user
Determin if interger is positive or negative
if the number is positive, display multiplication table
if number is negative, tell user program cannot accept it
Ask user to run again?
If yes, run program
If no, end program
'''

run_again = 'yes'

while run_again !="no":

    user_num = int(input("Enter an integer: "))

    if user_num >= 0:
        #display multiplication for that value and range (10-12)
        for item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")
    else:
        print("This program does not handle negative values")

    run_again = input("Would you like to run the program again? ")

#Loop has broken. User entered 'no'
print("Program is ending....")



