# Darion Poole
# 04/15/2025
# P2HW2
# Creating code for expenses

# Enter Module Test List

print('Test Grading Tool')
print('-----------------------------')
print('\n')

Module1 = float(input('Enter Module 1 Grade: '))

Module2 = float(input('Enter Module 2 Grade: '))

Module3 = float(input('Enter Module 3 Grade: '))

Module4 = float(input('Enter Module 4 Grade: '))

Module5 = float(input('Enter Module 5 Grade: '))

Module6 = float(input('Enter Module 6 Grade: '))

#Create List of Test Scores

Student_Test_Grade_List = [Module1, Module2, Module3, Module4, Module5, Module6]
print('\n')

#Enter results of test calculations

print('-----------Results-----------')

Average = sum(Student_Test_Grade_List) / len(Student_Test_Grade_List)
Lowest_Grade = min(Student_Test_Grade_List)
Highest_Grade =max(Student_Test_Grade_List)

# Output of Program calculations
print(f'{'Lowest Grade:':<15} {Lowest_Grade:}')
print(f'{'Highest Grade:':<15} {Highest_Grade:.1f}')
print(f'{'Sum of Grades:':<15} {sum(Student_Test_Grade_List)}')
print(f'{'Average:':<15} {Average:.1f}')

                                    
