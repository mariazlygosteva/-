distance_cm = float(input('Введите расстояние в сантиметрах: '))
distance_inches = distance_cm / 2.54
distance_feet = distance_inches / 12
distance_yards = distance_feet / 3
distance_miles = distance_yards / 1760
print(f'Расстояние в ярдах: {distance_yards}')
print(f'Расстояние в милях: {distance_miles}')
print(f'Расстояние в футах: {distance_feet}')
print(f'Расстояние в дюймах: {distance_inches}')