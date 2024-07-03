#Crie um programa para o Boletim de notas do aluno. Guarde o nome do aluno, as notas e calcule a media final do aluno.
nome= input('Digite o seu nome: ')
mat = input('Digite a sua nota na disciplina de matemática: ')
mat = float(mat)

por = input('Digite a sua nota na disciplina de português: ')
por= float(por)

geo = input('Digite a sua nota na disciplina de geografia: ')
geo = float(geo)

his = input('Digite a sua nota na disciplina de história: ')
his = float(his)

fis = input('Digite a sua nota na disciplina de física: ')
fis = float(fis)
print('')
media = (mat + por + geo + his+fis) / 5

#Ao obter as notas e a media das notas, imprima o boletim do aluno informando as notas das matérias e com quanto ele ficou de média

print(10*'-' +' BOLETIM ESCOLAR '+ 10*'-')
print(f'Nome do aluno: {nome} ')
print(f'Nota em Matemática: {mat} ')
print(f'Nota em Português: {por} ')
print(f'Nota em Geografia: {geo} ')
print(f'Nota em História: {his} ')
print(f'Nota em Física: {fis} ')
print(f'Média final: {media:.2f}')
print(37*'-')
