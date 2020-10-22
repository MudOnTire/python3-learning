ninja_belts = {
    'crystal': 'red',
    'ryu': 'black'
}

print(ninja_belts['crystal'])

print('yoshi' in ninja_belts)

print(ninja_belts.keys())

print(ninja_belts.values())

print(list(ninja_belts.keys()))

vals = list(ninja_belts.values())

print(vals)

print(vals.count('black'))

# add new key-value
ninja_belts['yoshi'] = 'red'

print(ninja_belts)

# other way to defind a dictionary
person = dict(name='shaun', age=30, height='6ft')

print(person)