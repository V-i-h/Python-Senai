import os

nome = input('Digite seu nome: ')
idade =int(input('Digite a sua idade: '))  

os.system('cls')

while True:
    print(20*'-','CINE PIPOCA',20*'-')
    print(10*'-','Sala 1 - Divertidamente 2(L)')
    print(10*'-','Sala 2 - Kung fu Panda (L)')
    print(10*'-','Sala 3 - Bad Boys 4 (16)')
    print(10*'-','Sala 4 - Um tira da pesada (12)')
    print(10*'-','Sala 5 - Super Mario Boss(L)')
    
    sala = int(input('Digite a sala desejada: '))
    #Sala 1
    if sala == 1  :
        print(10*'-','Ingresso',10*'-')
        print('Filme: Divertidamente 2')
        print(f'{nome}, pode se direcionar para a sala 1')
        break

    #Sala 2
    elif sala == 2  :
        print(10*'-','Ingresso',10*'-')
        print('Filme: Kung Fu Panda')
        print(f'{nome}, pode se direcionar para a sala 2')
        break

    #Sala 3
    elif sala == 3 and idade >= 16 :
        print(10*'-','Ingresso',10*'-')
        print('Filme: Bad Boys 4')
        print(f'{nome}, pode se direcionar para a sala 3') 
        break

    #Sala 4    
    elif sala == 4 and idade >= 12 :
        print(10*'-','Ingresso',10*'-')
        print('Filme: Um tira da pesada')
        print(f'{nome}, pode se direcionar para a sala 4')
        break
        
    #Sala 5
    elif sala == 5 :
        print(10*'-','Ingresso',10*'-')
        print('Filme: Super Mario Boss ')
        print(f'{nome}, pode se direcionar para a sala 5')
        break

    else:
        print(f'{nome} não tem idade suficiente para assistir o filme, escolha outro filme \n')
        continue
    
    

   


