def even_list(num_list):

    new_list = [val for val in num_list if val%2==0]
    print(new_list)


even_list([1,2,3,4,5,6,7,8])