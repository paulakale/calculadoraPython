# -- coding: utf-8 --#
"""
calculadora
autora: paula
objetivos: soma, divisao, multiplicacao, subtracao.
"""

print ("---------- Minha primeira calculadora <3 ----------")
num1 = input ("Digite o primeiro número: ")
num1 = int(num1)
operador = input ("Digite o operador: ")
num2 = input ("Digite o segundo número: ")
num2 = int(num2)

# + soma
if operador == "+":
    operacao = num1 + num2

# - subtracao
if operador == "-":
    operacao = num1 - num2
# * multiplicacao
if operador == "*":
    operacao = num1 * num2
# / divisao
if operador ==  "/":
    operacao = num1/num2

print ("O resultado é: ")
print (operacao)