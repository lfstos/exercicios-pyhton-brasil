def sexo():
    sex = input('Digite M ou F: ')
    if sex.lower() == 'm':
        return 'Masculino'
    elif sex.lower() == 'f':
        return 'Feminino'
    else:
        return 'Sexo inválido'

if '__main__' == __name__:
    sex = sexo()
    print(sex)