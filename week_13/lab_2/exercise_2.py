def sum_tuple(values):
    tot_sum = 0
    for value in values:
        tot_sum += value
    return tot_sum

print(sum_tuple((1,2,3))) # Expected 6
print(sum_tuple((5,-2,10))) # Expected 13