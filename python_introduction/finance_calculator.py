# User Input for Financial Details
monthly_income = float(input("Enter your monthly income: "))  
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings
interest_rate = 0.05
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * interest_rate) 

# Output Results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
