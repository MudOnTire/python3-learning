def greet(name='bruce', time='morning'):
    print(f'Good {time} {name}, hope you are well')


name = input('enter your name: ')
time = input('enter the time of a day: ')

greet(name, time)
