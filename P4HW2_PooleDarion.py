# Darion Poole
# 04/25/25
# P4HW2
# Calculate gross pay for multiple employees, determined by user,
# and also calculates total amount paid for overtime,
# total amount paid for regular pay and total amount paid for all employees.
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

#Request employee information
name = input("Enter employee's name or 'Done' to terminate: ")

while name.lower() !="done":
    hours_worked = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employees pay rate: "))

    print("-------------------------\n")


#Evaluate overtime

    if hours_worked > 40:
        #calculate overtime
        overtime_hours = hours_worked -40
        #calculate over pay
        over_pay = overtime_hours * (pay_rate * 1.5)
        #calculate salary for regular hours
        reg_pay = 40 * pay_rate
    else:
        over_pay = 0
        overtime_hours = 0
        reg_pay = hours_worked * pay_rate
        

    #calculate gross pay
    gross_pay = reg_pay + over_pay
    


    #Display results

    print("Employee Name: ", name, "\n")
    print(f'{"Hours Worked":<15}{"OverTime":<15}{"OverTime Pay":<15}{"$"}{"RegHour Pay ":<15}{"$"}{"Gross Pay":<15}')
    print("---------------------------------------------------------------------------")
    print(f'{hours_worked:<17}{overtime_hours:<17}{over_pay:<13}{reg_pay:<15.2f}{gross_pay:<15.2f}')       
    
    total_overtime_pay += over_pay
    total_regular_pay += reg_pay
    total_gross_pay += gross_pay
    employee_count += 1
    print()
    name = input("Enter employee's name or 'Done' to terminate: ")
print()

#Show final Results for Total
print(f'Total number employees entered: {employee_count}')
print(f'Total amount for overtime: ${total_overtime_pay:.2f}')
print(f'Total amount for regular hours: ${total_regular_pay:.2f}')
print(f'Total amount paid in gross: ${total_gross_pay:.2f}')



