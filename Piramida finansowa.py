
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Błąd: Wprowadź liczbę.")

def calculate_tax(salary):
    if salary <= 10000:
        return salary * 0.05
    elif salary <= 40000:
        return salary * 0.10
    elif salary <= 80000:
        return salary * 0.15
    else:
        return salary * 0.20

def main():
    print("----- FINANCIAL VISUALIZER -----")

    salary = get_float_input("Roczna pensja: ")
    housing = get_float_input("Miesięczne koszty mieszkania: ") * 12
    bills = get_float_input("Miesięczne rachunki: ") * 12
    food = get_float_input("Tygodniowe wydatki na jedzenie: ") * 52
    travel = get_float_input("Roczne wydatki na podróże: ")

    tax = calculate_tax(salary)
    total_expenses = housing + bills + food + travel + tax
    extra = salary - total_expenses

    def calculate_percentage(amount):
        return round((amount / salary) * 100, 1)

    expenses = {
        "mieszkanie": housing,
        "rachunki": bills,
        "jedzenie": food,
        "podróże": travel,
        "podatki": tax,
        "reszta": extra
    }

    percentages = {k: calculate_percentage(v) for k, v in expenses.items()}

    print("Podsumowanie finansów:")
    print("-----------------------------")

    for category, amount in expenses.items():
        bar = "#" * int(percentages[category])
        print(f"{category:<10} | {amount:>10.2f} zł | {percentages[category]:>5.1f}% | {bar}")

    print("-----------------------------")

if __name__ == "__main__":
    main()
