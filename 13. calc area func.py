def area(radius):
    return 3.1415926 * radius**2


def vol(area, length):
    print(area * length)


radius = int(input('enter a radius: '))
length = int(input('enter a length: '))

area_calc = area(radius)
vol(area_calc, length)
