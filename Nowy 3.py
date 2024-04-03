revenue = int (input ('Biznes revenue: '))
cost = int (input ('Biznes costs: '))
profit = revenue - cost
print ('Biznes profit to: ' + str(profit))
cost_bar = '#' * int ((cost / revenue) * 25)
profit_bar = '#' * int ((profit / revenue) * 25)
print ('  cost: ' + cost_bar)
print ('profit: ' + profit_bar)
