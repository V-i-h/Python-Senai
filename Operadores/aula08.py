'''import os
import time

cont = int(input('Digite um número inteiro: '))

while cont >=0:
    os.system('cls')#Limpar o terminal
    print(f'Contagem regressiva: {cont}....')
    time.sleep(1)#Atrasa o próximo comando
    cont -= 1

os.system('cls')
print('BOOOOOOOOOOOOOOOOOOOOMMMMMMMM!!!!!1')


print(30*'-','CALCULADORA DE IMC' ,30*'-')
while True:
    opcao = input('Deseja calcular o seu imc ?(s/n) ').upper()
    
    if opcao != 'N':
        peso = input('Digite o seu peso: ').replace(',','.')
        peso = float(peso)
        altura = input('Digite a sua altura: ').replace(',','.')
        altura= float(altura)
        calculo = peso/(altura*altura)

        if calculo <=17 :
            print(f'Seu IMC: {calculo}\nSituação: Está com anorexia')
        elif  calculo > 17 and calculo <= 18.5:
            print(f'Seu IMC: {calculo}\nSituação: Está abaixo do peso')
        elif calculo > 18.5 and calculo <= 25:
            print(f'Seu IMC: {calculo}\nSituação: Está com o peso ideal')
        elif calculo >25 and calculo <= 30:
            print(f'Seu IMC: {calculo}\nSituação: Está acima do peso')
        elif calculo >30 and calculo  <= 35:
            print(f'Seu IMC: {calculo}\nSituação: Está com grau de obesidade I')
        elif calculo >35 and calculo <= 40:
            print(f'Seu IMC: {calculo}\nSituação: Está com grau de obesidade II')
        else:
            print(f'Seu IMC: {calculo}\nSituação: Está com grau de obesidade mórbida')
        continue
    else:
        print('Não deseja mais calcular o IMC')
        break
    
'''


print(20*'-','Calculadora básica',20*'-')
while True:
    opcao = input('Deseja realizar um calculo ?(s/n) ').upper()

    if opcao != 'N':
         num1=input('Digite o primeiro número: ')
         num2 = input('Digite o segundo número: ')
         num1 = float(num1)
         num2 = float(num2)
         operacao = input('Digite a operação que deseja realizar: (+),(-),(/),(*)')
         if operacao == '+':
          print(f'A soma dos números {num1} + {num2} = {num1+num2}')
         elif operacao == '-':
          print(f'A subtração dos números {num1} - {num2} = {num1-num2}')
         elif operacao == '/':
          print(f'A divisão dos números {num1} / {num2} = {num1/num2}')
         elif operacao == '*':
          print(f'A multiplicação dos números {num1} * {num2} = {num1*num2}')
         else:
          print(f'Operação inválida!!')
    else:
      print('Não desejo mais realizar calculos!')
      break
5
