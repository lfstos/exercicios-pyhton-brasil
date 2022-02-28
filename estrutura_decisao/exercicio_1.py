def maior_numero():
    valor_1 = int(input('Digite um valor: '))
    valor_2 = int(input('Digite outro valor: '))

    if valor_1 > valor_2:
        return valor_1
    else:
        return valor_2

if '__main__' ==__name__:
    maior = maior_numero()
    print(maior)
