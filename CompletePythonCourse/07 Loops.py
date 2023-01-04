employees = {'ABC': 1000, 'PQR': 2000, 'XYZ': 1500}

for (name, salary) in employees.items():
    print(name, 'has salary USD', salary)


employees = [('ABC', 1000), ('PQR', 2000), ('XYZ', 1500)]

for name, salary, age in employees: # if tuple has 2 values, here we need 2 variables
    print(name, 'has salary USD', salary)

