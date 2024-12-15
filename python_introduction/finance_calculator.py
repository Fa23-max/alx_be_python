Monthlyincome = int(input("Enter your monthly income:"))
MonthlyExpenses = int(input("Enter your total mountly expenses:"))
Monthlysavings =  Monthlyincome - MonthlyExpenses
Projectedsavings =  Monthlysavings * 12 + (Monthlysavings * 12 * 0.05)
print(F"Your monthly savings are ${Monthlysavings}")
print(F"Projected savings after one year, with interest, is: ${Projectedsavings}")
