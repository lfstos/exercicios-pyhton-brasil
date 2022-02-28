def notas():
    n1 = float(input('Entre com a nota 1: '))
    n2 = float(input('Entre com a nota 2: '))

    media = (n1 + n2) / 2

    if media > 7.0:
        return 'Aprovado'
    elif media == 7.0:
        return 'Aprovado com distinção'    
    else:
        return 'Reprovado'

if '__main__' == __name__:
    print(notas())