weight = input('Enter your weight: ')
unit = input('(L)bs of (K)g: ')
if unit.lower() == 'l':
    print(f'{float(weight) * (0.453592)} Kg')
elif unit.lower() == "k":
    print(f'{float(weight) * (2.20462)} Lbs')