earned_amount = 'Earned amount:'

bubblegum = 202
toffee = 118
ice_cream = 2250
milk_chocolate = 1680
doughnut = 1075
pancake = 80

print(earned_amount)
print(f"Bubblegum: ${bubblegum}")
print(f"Toffee: ${toffee}")
print(f"Ice cream: ${ice_cream}")
print(f"Milk chocolate: ${milk_chocolate}")
print(f"Doughnut: ${doughnut}")
print(f"Pancake: ${pancake}")
print()

income = bubblegum + toffee + ice_cream + milk_chocolate + doughnut + pancake
print(f'Income: ${income}')
staff_expenses = int(input("Staff expenses: \n"))
other_expenses = int(input("Other expenses: \n"))

net_income = income - (staff_expenses + other_expenses)
print(f"Net income: ${net_income}")