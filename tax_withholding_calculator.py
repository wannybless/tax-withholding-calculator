# Get the weekly income from the user
weekly_income = float(input("Enter your weekly income: "))

# Calculate the tax rate based on the income
if weekly_income < 500:
  tax_rate = 0.10
elif weekly_income >= 500 and weekly_income < 1500:
  tax_rate = 0.15
elif weekly_income >= 1500 and weekly_income < 2500:
  tax_rate = 0.20
else:
  tax_rate = 0.30

# Calculate the tax withholding
tax_withholding = weekly_income * tax_rate

# Print the result
print("Your weekly tax withholding is: ${:.2f}".format(tax_withholding))
