import sys
in_values = sys.argv[1:]
new_values = []
income = 0
outcome = 0
for item in in_values:
    if int(item) >= 0:
        income += int(item)
    else:
        outcome += int(item)
print("Доходы: {} руб.".format(income))
print("Расходы: {} руб.".format(abs(outcome)))