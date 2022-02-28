from unicodedata import name
from pip import main


def vogal_consoante():
    letra = input('Digite um caracter: ')
    vogal = 'aeiou'
    if letra in vogal:
        return 'Vogal'
    else:
        if len(letra) > 1:
            return 'Opção inválida'
        else:    
            return 'Consoante'
            

if '__main__' == __name__:
    letra = vogal_consoante()
    print(letra)