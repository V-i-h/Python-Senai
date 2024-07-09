import random

num_secreto = random.randint(1,10)

# FIXME:Declarando variáveis 

tentativas = 0
max_tentativas = 5
acertou = False

print("Bem-vindo ao Game Python Adivinha!!! ")
print(f"Você tem {max_tentativas} para adivinhar o número secreto entre 1 e 20" )

#Loop (jogo)



while tentativas < max_tentativas: 
     palpite = input('Digite um número inteiro: ')
     palpite = int(palpite)

     tentativas += 1


     if palpite == num_secreto:
          acertou = True
          break
     elif palpite  < num_secreto :
          print('Tente um número maior ')
     else: 
          print('Tente um número menor')
if acertou:
     print(f'Parabéns! você acertou o número secreto: {num_secreto} em {tentativas} tentativas') 
else:
     print(f'Que pena, você não conseguiu adivinhar o numero secreto: {num_secreto}')         
     
    