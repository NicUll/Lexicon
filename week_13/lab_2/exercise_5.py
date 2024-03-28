
def only_even(in_list):
    return [val for val in in_list if val%2==0]

print(only_even([1,2,3])) # Expected output [2]
print(only_even([13,14,18,20,21,32])) # Expected ouput [14,18,20,32]