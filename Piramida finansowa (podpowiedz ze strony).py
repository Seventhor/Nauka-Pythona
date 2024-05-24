print('--------------------------------')
print('----- FINANCIAL VISUALIZER -----')
print('--------------------------------')
salary = input('Annual Salary:\n')
housing = input('Monthly Housing:\n')
bills = input('Monthly Bills:\n')
food = input('Weekly Food:\n')
travel = input('Annual Travel:\n')

# Check if the 5 input values can be converted to a floating-point number
# If so, convert them
def isinvalid(x):
    for i in x:
        if i.isnumeric() == False and i != '.':
            return True
    return False

if isinvalid(salary) or isinvalid(housing) or isinvalid(bills) or isinvalid(food) or isinvalid(travel):
    print('Invalid input, please try again.')
else:
    print('All inputs confirmed valid.')
salary  = float(salary)
housing = float(housing)
bills   = float(bills)
food    = float(food)
travel  = float(travel)

# Compute the annual tax
annual_tax = 0
if salary <= 10000:
    annual_tax = round(salary * 0.05, 2)
elif salary <= 40000:
    annual_tax = round(salary * 0.1, 2)
elif salary <= 80000:
    annual_tax = round(salary * 0.15, 2)
else:
    annual_tax = round(salary * 0.20, 2)

# Calculate the annual dollar amounts and the annual percentages
annual_housing = housing * 12
annual_bills = bills * 12
annual_food = food * 52
annual_travel = travel
annual_extra = salary - annual_housing - annual_bills - annual_food - annual_travel - annual_tax
percentage_tax = round((annual_tax / salary) * 100, 1)
percentage_housing = round((annual_housing / salary) * 100, 1)
percentage_bills = round((annual_bills / salary) * 100, 1)
percentage_food = round((annual_food / salary) * 100, 1)
percentage_travel = round((annual_travel / salary) * 100, 1)
percentage_extra = round((annual_extra / salary) * 100, 1)

# Display the grid with financial information and bar chart
width = int(max(percentage_tax, percentage_housing, percentage_bills, percentage_food, percentage_travel, percentage_extra))
boundary = '----------------------------------' + ('-' * width)
print()
print(boundary)
print('housing | $' + format(annual_housing, '11,.2f') + ' ', end='')
print('| ' + format(percentage_housing, '5,.1f') + '% | ' + ('#' * int(percentage_housing)))
print('  bills | $' + format(annual_bills, '11,.2f') + ' ', end='')
print('| ' + format(percentage_bills, '5,.1f') + '% | ' + ('#' * int(percentage_bills)))
print('   food | $' + format(annual_food, '11,.2f') + ' ', end='')
print('| ' + format(percentage_food, '5,.1f') + '% | ' + ('#' * int(percentage_food)))
print(' travel | $' + format(annual_travel, '11,.2f') + ' ', end='')
print('| ' + format(percentage_travel, '5,.1f') + '% | ' + ('#' * int(percentage_travel)))
print('    tax | $' + format(annual_tax, '11,.2f') + ' ', end='')
print('| ' + format(percentage_tax, '5,.1f') + '% | ' + ('#' * int(percentage_tax)))
print('  extra | $' + format(annual_extra, '11,.2f') + ' ', end='')
print('| ' + format(percentage_extra, '5,.1f') + '% | ' + ('#' * int(percentage_extra)))
print(boundary)
