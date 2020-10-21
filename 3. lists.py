fib1 = [1, 1, 2, 3, 5, 8, 13]

# get element
fib1[1]  # 1

# slice
fib1[0:4]  # [1,1,2,3]

# concatnation
fib2 = [21, 34, 55]
fib1 + fib2  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# change element
fib1[0] = 9

# append
fib1.append(21)

# pop
fib1.pop()

# remove
fib1.remove(8)  # only remove one element

# delete, remove with index
del(fib1[0])

# mix data types
chars = ['mario', 'luigi', 'bowser']
chars.append(5)

# list in list
nums = [chars, fib1, [1, 2, 3, 4]]
