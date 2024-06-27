def compute_tax(income, credits):
    net = income - credits
    tax = 0
    remaining = 0
    if net < 50000:
        tax = net * 0.15
    elif net < 100000:
        tax = net * 0.20
    remaining = net - tax
    return tax, remaining
