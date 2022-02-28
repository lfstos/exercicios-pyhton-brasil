peso = float(input('Peso de peixe: '))

if peso > 50:
    excesso = (50 - peso) * 4
    print('Valor a ser pago por kg excedente {0:.2f}'.format(excesso))