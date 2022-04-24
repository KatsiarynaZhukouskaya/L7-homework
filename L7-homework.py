# задача №1

a = [1, 3, 4, 5, 6, 4, 3, 2, 1, 6, 7, 4, 2, 5, 6, 4, 2, 1, 2, 2, 2, 4, 9, 7, 6, 8]

def my_func(a):
    my_dict2 = {}
    for key in a:
        my_dict2[key] = my_dict2.get(key, 0) +1
    print(my_dict2)
my_func(a)

