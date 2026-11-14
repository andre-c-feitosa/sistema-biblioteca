# Nome do Projeto: Sistema de Empréstimos da Biblioteca

# Numero do Grupo: 04

# Nome dos integrantes e número das matriculas, respectivamente:
#    - André Cristian -> 126100318
#    - Luis Felipe ->
#    - Matheus Victor -> 
#    - João Gabriel Lima -> 

# O valor de K é igual a 37!

# Bloco Feito pro André Cristian 
print('=========================================')
print('BEM VINDO AO SISTEMA DA BIBLIOTECA UNIFSA')
print('=========================================')
print('1- Cadastrar Livro\n2- Cadastrar usuário\n3- Registrar empréstimo\n4- Registrar devolução\n5- Listar os livros disponíveis\n6- Listar os livros emprestados\n7- Listar os empréstimos atrasados\n')
resultado = int(input('Qual serviço você deseja (Selecione o número ao lado do serviço) ?: '))

bibliteca = []

def cadastrar_livro():   
    print('\nPara cadastrar o livro você precisa das seguites informações: ')

    código = input('Código do livro: ') 
    titulo = input('Título do livro: ') 
    autor = input('Autor do Livro: ')

    tratamento_situacao = input('\nO livro está disponível ? [s/n]: ').lower()
    if (tratamento_situacao == 's'):
        situacao = print('Disponível')
    else:
        situacao = print('Emprestado')

    novo_livro = {
        'Código: ': código,
        'Título: ': titulo,
        'Autor: ': autor,
        'Situação: ': situacao
    }
    
    bibliteca.append(novo_livro)
            
    return 'Livro cadastrado com sucesso!!'

match resultado:
    case 1:
        cadastro = input('\nVocê deseja cadastrar um livro [s/n] ?:').lower()

        if (cadastro == 's'):
            mensagem = cadastrar_livro()
            print(mensagem)
        elif (cadastro == 'n'):
            print('Tudo bem, volte quando precisar cadastrar um livro!')
        else:
            print('Você digitou uma resposta invalida. Reinicie o sistema e tente novamente.')
    case 2:
        print('Cadastre o usuário')
    case 3:
        print('Resgistre o emprestimo do livro')
    case 4:
        print('Registre a devolução do livro')
    case 5:
        print('Vou listar todos os livros disponíveis')
    case 6:
        print('Vou listar todos os livros que foram emprestados')
    case 7:
        print('Vou listar todos os emprestimos atrasados')
    case _:
        print('Você selecionou um serviço inválido')

