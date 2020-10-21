my_name = 'bruce' # global variable


def print_name():
    # override the global variable
    global my_name
    my_name = 'crixus'
    print('the name inside the function is', my_name)


print_name()

print('outside the function, the name is', my_name)
