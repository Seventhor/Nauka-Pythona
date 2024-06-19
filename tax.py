
def calculate_tax(salary):
    if salary <= 10000:
        return salary * 0.05
    elif salary <= 40000:
        return salary * 0.10
    elif salary <= 80000:
        return salary * 0.15
    else:
        return salary * 0.20