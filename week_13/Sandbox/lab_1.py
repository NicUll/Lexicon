

def exercise_1():
    test_str = 'Python'
    print(test_str[4])
    print(test_str[:4])
    print(test_str[1:4])
    print(test_str[::-1])


def exercise_2():
    l = [3,7,[1,4,'hello']]
    print(f'Before change: l = {l}')
    l[2][2] = "goodbye"
    print(f'After change: l = {l}')

def exercise_3():
    d1 = {'simple_key':'hello'}
    d2 = {'k1':{'k2':'hello'}}
    d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

    print(d1['simple_key'])
    print(d2['k1']['k2'])
    print(d3['k1'][0]['nest_key'][1][0])

def exercise_4():
    mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
    print(set(mylist))

def exercise_5():
    age = 4
    name = "Sammy"
    print("Hello my dog's name is {} and he is {} years old".format(name, age))
    print("Hello my dog's name is {name} and he is {age} years old".format(name=name, age=age))
    print(f"Hello my dog's name is {name} and he is {age} years old")


exercise_1()
exercise_2()
exercise_3()
exercise_4()
exercise_5()
