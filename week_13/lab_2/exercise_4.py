def merge_dict(dict_1:dict, dict_2:dict):
    dict_1.update(dict_2)
    return dict_1

dict_a = {1:"One", 2:"Two"}
dict_b = {3:"Three", 4:"Five"}
dict_c = {4:"Four", 6:"Six"}

print(f'dict_a: {dict_a}')
print(f'dict_b: {dict_a}')
dict_ab = merge_dict(dict_a, dict_b)
print(f'dict_ab: {dict_ab}') # Expected output dict_ab: {1: 'One', 2: 'Two', 3: 'Three', 4: 'Five'}
dict_abc = merge_dict(dict_ab, dict_c)
print(f'dict_abc: {dict_abc}') # Expected output dict_abc: {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 6: 'Six'}