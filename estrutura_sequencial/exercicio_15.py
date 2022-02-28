def ganho_hora():
    salario = float(input('Ganho por hora: '))
    horas_tabalhadas = float(input('Horas trabalhadas mês: '))
    IR = 0.11
    INSS = 0.08
    SINDICATO = 0.05
    
    descontos = IR + INSS + SINDICATO
    
    salario_bruto = salario * horas_tabalhadas
    
    pago_ir = salario_bruto * IR
    pago_inss = salario_bruto * INSS
    pago_sindicato = salario_bruto * SINDICATO
    salario_liquido = salario_bruto - (salario_bruto * descontos)

    print('Salario Bruto {0:0.2f}'.format(salario_bruto))
    print('IR {0:0.2f}'.format(pago_ir))
    print('INSS {0:0.2f}'.format(pago_inss))
    print('Sindicato {0:0.2f}'.format(pago_sindicato))
    print('Salário liquido {0:0.2f}'.format(salario_liquido))


if '__main__' == __name__:
    ganho_hora()
