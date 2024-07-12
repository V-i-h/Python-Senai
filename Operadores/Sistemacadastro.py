import time
lista_cpf =['123.321.231-12']
lista_nome = ['gomes']

while True:
    print(30*'=','BEM-VINDO AO PYTHON CADASTRO',30*'=')
    print('1. Cadastrar um novo usuáro')
    print('2. Acessar o sistema')
    print('3 Listar os usuários ')
    print('4. Excluir usuário')
    print('5. Sair')


    opcao = input('Digite a opção: ')
    print()
    if opcao == '1':

        novo_nome = input('Digite um novo nome que deseja cadastrar: ')
        novo_cpf =  input('Digite um novo CPF: ')

        if novo_cpf in lista_cpf:
            print('CPF já está cadastrado')
        else:
            lista_cpf.append(novo_cpf)
            lista_nome.append(novo_nome)
            print('CPF cadastrado com sucesso!')

    elif opcao =='2':
        cpf = input('Digite seu CPF: ')
        if cpf in lista_cpf:
            print('Usuário logado com sucesso!')
        else:
            print('CPF inválido!')

    elif opcao  == '3':
        print('Lista dos usuários ')
        for i in lista_nome:
            print(f'Usuário: {i}')
        
    elif opcao =='4':

        excluir_cpf = input('Digite o CPF que você deseja excluir: ')
        if excluir_cpf in lista_cpf:
            lista_cpf.remove(excluir_cpf)
            print('CPF removido com sucesso!')
        else:
            print('CPF inválido!')        

    elif opcao == '5':
        print('Saindo do sistema !')
        time.sleep(3)
        break
    else: 
        print('Opção inválida!')