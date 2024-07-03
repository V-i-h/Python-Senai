"""
n1 = input('Digite o primeiro número: ')
n2 = input('Digite o segundo número: ')

#Convertendo as entradas para inteiro 
n1 =int(n1)
n2 =int(n2)

divisao_inteira = n1 // n2
divisao = n1/n2
resto = n1 % n2
expo = n1 ** n2 

print(f'Divisão inteira:{divisao_inteira} ')
print(f'Divisão normal:{divisao} ')
print(f'Resto: {resto}')
print(f'Exponenciação: {expo}\n') 
"""

#Atribuição de subtração
valor = 10
valor -= 10
print(f'Resultado de atribuição de subtração: {valor}')

#Atribuição de soma
valor += 10
print(f'Resultado de atribuição de soma: {valor}')

#Atribuição de multiplicação
valor *= 10
print(f'Resultado de atribuição de multiplicar: {valor}')

#Atribuição de divisão normal
valor /= 10
print(f'Resultado de atribuição de divisão normal: {valor}')

#Atribuição de divisão inteira
valor //=10
print(f'Resultado de atribuição de divisão inteira: {valor}')

#Atribuição de modulo
valor %= 10
print(f'Resultado de atribuição de modulo: {valor}')

