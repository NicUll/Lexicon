
#### Only 1,2,3 ####
def s_array_check(check_list):
    for i in range(len(check_list)-2):
        if check_list[i] == 1:
            if (check_list[i+1] == 2) and (check_list[i+2] == 3):
                return True
    return False

#print(s_array_check([4,5,6,1,2,3,7]))
#print(s_array_check([1,2,4,5,7]))
####################

#### Expanding exercise 1 - Any list against any list ####
def _recur_check(ref_list, check_list):
    if not ref_list: # No more values to check
        return True
    if ref_list[0] == check_list[0]:
        return _recur_check(ref_list[1:], check_list[1:])
    return False

def array_check(ref_list, check_list):
    element_amount = len(ref_list)
    iter_length = len(check_list) - element_amount + 1
    if (not ref_list) or (iter_length <= 0): # If empty reference list or smaller than check_list
        return False
    for i in range(iter_length):
        if check_list[i] == ref_list[0]:
            if _recur_check(ref_list[1:], check_list[i+1:]):
                return True
    return False


print(array_check([1,2,3], [1,2,3,4])) # Expected True
print(array_check([1,2,3], [2,3,4])) # Expected False
print(array_check([1,2,3], [5,6,7,1,2,3,8,9])) # Expected True
print(array_check([], [1,2,3,4])) # Testing empty reference, expected False
print(array_check([1,2,3,4], [1,2,3])) # Testing check list shorter than ref, expected False
print(array_check([1,2,3],[]))
