monthly_income = [5000]
monthly_expenses = [4000]

monthly_savings = monthly_income - monthly_expenses

projected_savings = monthly_savings * 12 + {monthly_savings * 12 * 0.05}

print(f"The user’s monthly savings is {monthly_savings}")
print(f"The projected annual savings after including interest is {projected_savings}")
