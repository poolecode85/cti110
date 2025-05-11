# Darion Poole
# 04/20/25
# P3HW2
# Creating program to calculate overtime

#Request employee information
name = input("Enter Employee Name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employees pay rate: "))
print("-------------------------")
("\n")

#Evaluate overtime

if hours_worked > 40:
    #calculate overtime
    overtime_hours = hours_worked -40
    #calculate over pay
    over_pay = overtime_hours * (pay_rate * 1.5)
    #calculate salary for regular hours
    reg_pay = 40 * pay_rate
    #calculate gross pay
    gross_pay = reg_pay + over_pay

else:
    over_pay = 0
    overtime_hours = 0
    reg_pay = hours_worked * pay_rate

print("Employee Name: ", name, "\n")
print(f'{"Hours Worked":<15}{"OverTime":<15}{"OverTime Pay":<15}{"$"}{"RegHour Pay ":<15}{"$"}{"Gross Pay":<15}')
print("---------------------------------------------------------------------------")
print(f'{hours_worked:<17}{overtime_hours:<17}{over_pay:<13}{reg_pay:<15.2f}{gross_pay:<15.2f}')       


