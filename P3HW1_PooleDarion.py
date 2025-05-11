# Darion Poole
# 04/020/2025
# P3HW1
# Creating code for grades using if/else


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))
print('\n')

# add grades entered to a list

Grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

Lowest_Grade = min(Grades)
Highest_Grade = max(Grades)
Average = sum(Grades) / len(Grades)

# determine letter grade for average
print('----------Results----------')

print(f'{'Lowest Grade:':<15} {Lowest_Grade:}')
print(f'{'Highest Grade:':<15} {Highest_Grade:.1f}')
print(f'{'Sum of Grades:':<15} {sum(Grades)}')
print(f'{'Average:':<15} {Average:.1f}')
print('---------------------------')
if Average >= 90:
    print('Your grade is: A')
elif Average >= 80:
    print('Your grade is: B')
elif Average >= 70:
    print('Your grade is: C')
else:
    print('Your grade is: F')

# TO DO: finish this







