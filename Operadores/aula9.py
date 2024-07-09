#Árvore de natal
'''
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

pa = termo+(20-1)* razao

for i in range(termo, pa+razao, razao):
    print(i)
    

altura = 20
espacamento = 0
asterisco = 1
simbolo= '*'
for i in range(altura):
    espacamento = altura - i- 1

    for j in range (espacamento):
        print(' ', end='')

    for k in range(asterisco):
        print(simbolo,end='')

    print()
    asterisco +=2
    '''

#Sorteio aleatorio de nomes
'''
import random
import os
lista_nome=[]
lista_sorteados =[]
while True:
    nome = input('Digite os nomes que serão sorteados: ')

    if nome != '':
        lista_nome.append(nome)
    else:
        break

while True:
    if lista_nome:
        os.system('cls')
        escolhido = random.choice(lista_nome)
        lista_sorteados. append(escolhido)
        lista_nome.remove(escolhido)
        print(f'O sorteado é: {escolhido}')

        opcao = input('Deseja sortear outro nome ? (s/n)').lower()
        os.system('cls')

        if opcao != 's':
            break
    else:
        print('Não existe nomes para serem sorteados')
    

print('Programa finalizado')
print(f'Lista dos nomes:{lista_nome}')
print(f'Lista dos sorteados:{lista_sorteados}')
'''   


#Lista
'''
lista = ['Gomes','Oliveira', 'Karython','Maria','Eduarda']
print(f'O primeiro nome da lista: {lista[0]}')
print(f'O segundo nome da lista: {lista[1]}')
print(f'O terceiro nome da lista {lista[2]}') 
'''


lista = ['Gomes','Oliveira', 'Karython','Maria','Eduarda']

for i in range(5):
    print(f'{i+1}° nome : {lista[i]}')
print()

for i in range(len(lista)):
    print(f'{i+1}° nome: {lista[i]}')

#Tabuada
print(15*'-','TABUADA',15*'-')

x = int(input('Digite um número inteiro: '))

for num in range(1,11):
    print(f'{x} X {num} = {x* num}')
    
          



