def calc_power(base, exp):
    product = 1
    for i in range(exp):
        product *= base
    return product

print(calc_power(5,2)) # Expected 25
print(calc_power(10,0)) # Expected 1