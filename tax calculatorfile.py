num1 = float(input("enter undeducted salary>  "))
tax = float(input(" enter tax (for the current year !) >  "))
percentile = float(input(" enter pecentile>  "))

amount_deducted = print( num1 * tax / percentile)

new_salary = float(num1 + amount_deducted)

print(new_salary)



