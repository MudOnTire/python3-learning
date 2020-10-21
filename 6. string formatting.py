num1 = 3.1415926
num2 = 10.2324235978

# PREVIOUS
print('num 1 is', num1, 'and num 2 is', num2)

# FORMAT METHOD
print('num 1 is {} and num 2 is {}'.format(num1, num2))
print('num 1 is {0} and num 2 is {1}'.format(num1, num2))
print('num 1 is {1} and num 2 is {0}'.format(num1, num2))

# FORMAT OPTIONS
print('num 1 is {0:.3} and num 2 is {1:.3}'.format(num1, num2)) # 3 digits
print('num 1 is {0:.3f} and num 2 is {1:.3f}'.format(num1, num2)) # 3 decimal digits

# USING F-STRINGS
print(f'num 1 is {num1} and num 2 is {num2}')
print(f'num 1 is {num1:.4} and num 2 is {num2:.4}')
print(f'num 1 is {num1:.4f} and num 2 is {num2:.4f}')