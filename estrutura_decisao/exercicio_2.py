def positivo_negativo():
    num = int(input('Digite um valor: '))

    if num > -1:
        return 'Positivo'
    else:
        return 'Negativo'


if '__main__' == __name__:
    numero = positivo_negativo()
    print(numero)