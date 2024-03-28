def exercise_2():
    l = [3,7,[1,4,'hello']]
    print(f'Before change: l = {l}')
    l[2][2] = "goodbye"
    print(f'After change: l = {l}')