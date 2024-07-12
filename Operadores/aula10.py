nomes = ['Gomes','Oliveira','Lucas','José','Pedro','Maria','João']

'''
#Retornando elementos da lista atravez do indice
print(f'O primeiro nome é: {nomes[0]}')

#Retornando o ultimo elemento da lista
print(nomes[-1])


#Removendo item da lista com remove
nomes.remove('Lucas')
print(nomes)


#Removendo nome da lista com o pop

nomes.pop(0)
print(nomes)

#Removendo usando o Del

del nomes [2:4]

#Mostrando elementos atraves do intervalo

print(nomes[2:4])

#Adicionar um novo item na lista

nomes.append('Carlos')
print(nomes)

#Adicionar elemento em uma posição especifica

nomes.insert(2,'Josue')
print(nomes)

#Imprimindo a lista ignorando o Indice 0
for i in range(len(nomes)):
    print(f'{i+1}° nome da lista: {nomes[i]}')

#Recebendo um novo nome para adicionar na lista
novo_nome= input('Digite um novo nome a ser adicionado na lista: ')

#Recebendo uma posição para adicionar na lista
posicao = input('Informe  a posição desejada para adicionar um novo nome: ')

#Convertendo para int
posicao = int(posicao)

#Corrigindo a posição dos indices
posicao -= 1

if posicao >= 0 and posicao <= len(nomes):
    nomes.insert(posicao,novo_nome)
else:
    print('Posição inválida')
print()
print(30*'=','Lista Atualizada',30*'=')
for i in range(len(nomes)):
    print(f'{i+1}° nome da lista: {nomes[i]}')


#Atribuindo um novo valor para o índice 1 da lista

nomes = ['Gomes','Oliveira','Lucas','José','Pedro','Maria','João']

nomes[1] = 'Garoto de programa'
print(nomes)
'''
#Ordenando a Lista

lista1 = [10,9,8,7,6,5,4,3,2,1]

print(f'Lista desordenada: {lista1}')
lista1.sort()
print(f'Lista ordenada: {lista1}')

print()
#Lista ordenada decrescente

lista = [5,2,9,20,7,4,8,3,10,1]

print(f'Lista desordenada: {lista}')
lista.sort(reverse=True)
print(f'Lista ordenada Decrescente: {lista}')
