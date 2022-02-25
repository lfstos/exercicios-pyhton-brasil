h = float(input('Altura: '))
sexo = input('Digite M ou F: ')

if sexo.lower() == 'm':
    peso_ideal = (72.7 * h) - 58
    print('Seu peso ideal é {0:.2f}'.format(peso_ideal))
else:
    peso_ideal = (62.1 * h) - 44.7
    print(f'Seu peso ideal é {0:.2f}'.format(peso_ideal))
