def create_even_tuple(in_tuple):
    out_tuple = tuple(value for value in in_tuple if value%2==0)
    return out_tuple

print(create_even_tuple((1,2,3,4))) # Expected result (2,4)
print(create_even_tuple((3,5,7,9))) # Expected result ()
