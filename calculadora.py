# -- coding: utf-8 --#
"""
calculadora
autora: paula
objetivos: soma, divisao, multiplicacao, subtracao.
"""
sair = False
while sair == False:
    print ("---------- Minha primeira calculadora <3 ----------")
    num1 = input ("Digite o primeiro número: ")
    num1 = int(num1)
    operador = input ("Escolha o operador: 1. Soma; 2. Subtração; 3. Divisão; 4. Multiplicação: ")
    operador = int(operador)
    num2 = input ("Digite o segundo número: ")
    num2 = int(num2)

    # + soma
    if operador == 1:
        operacao = num1 + num2

    # - subtracao
    if operador == 2:
        operacao = num1 - num2

    # / divisao
    if operador ==  3:
        operacao = num1/num2

    # * multiplicacao
    if operador == 4:
        operacao = num1 * num2

    print ("O resultado é: ")
    print (operacao)

    teste = input ("Deseja sair? 1. Sim 2. Não: ")
    if teste == 1:
        sair = True