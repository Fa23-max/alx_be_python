monthly_income = float(input("Enter your monthly income:"))
monthly_expenses = float(input("Enter your total mountly expenses:"))
monthly_savings =  monthly_income - monthly_expenses
projected_savings =  monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(F"Your monthly savings are ${monthly_savings}")
print(F"Projected savings after one year, with interest, is: ${projected_savings}")
