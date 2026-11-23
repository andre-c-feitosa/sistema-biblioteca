# Nome do Projeto: Sistema de Empréstimos da Biblioteca

# Numero do Grupo: 04

# Nome dos integrantes e número das matriculas, respectivamente:
#    - André Cristian -> 126100318
#    - Luis Felipe ->
#    - Matheus Victor -> 
#    - João Gabriel Lima -> 

# O valor de K é igual a 37!

# Esqueleto do sistem feito por André Cristian
print('=========================================')
print('BEM VINDO AO SISTEMA DA BIBLIOTECA UNIFSA')
print('=========================================')
print('1- Cadastrar Livro\n2- Cadastrar usuário\n3- Registrar empréstimo\n4- Registrar devolução\n5- Listar os livros disponíveis\n6- Listar os livros emprestados\n7- Listar os empréstimos atrasados\n')
resultado = int(input('Qual serviço você deseja (Selecione o número ao lado do serviço) ?: '))

#Bloco Feito por André Cristian (livros cadastrados)
bibliteca = [
    {
        'Código:': '65110',
        'Título: ': 'Fundamentos da Inteligência Artificial',
        'Autor: ': 'João Luís Garcia Rosa',
        'Situação: ': 'Disponível',
    },
    {
        'Código:': '000525',
        'Título: ': 'Aprendendo Praticando',
        'Autor: ': 'Gorki Starlin',
        'Situação: ': 'Disponível',
    },
    {
        'Código:': '015899',
        'Título: ': 'Estrutura de Dados e Algoritmos',
        'Autor: ': 'Bruno R. Preiss',
        'Situação: ': 'Disponível',
    },
    {
        'Código:': '011412',
        'Título: ': 'Faça um Site, Flash Orientado a Objeto',
        'Autor: ': 'Carlos A. J. Oliviero',
        'Situação: ': 'Disponível',
    },
    {
        'Código:': '018094',
        'Título: ': 'Arquitetura de Redes de Computadores',
        'Autor: ': 'Luiz Paulo Maia',
        'Situação: ': 'Emprestado',
    },
    {
        'Código:': '078956',
        'Título: ': 'Interligação em Rede com TCP/IP',
        'Autor: ': 'Douglas E. Comer | David L. Stevens',
        'Situação: ': 'Emprestado',
    },
    {
        'Código:': '008695',
        'Título: ': 'Redes de Computadores Das LANs, MANs e WANs às Redes ATM',
        'Autor: ': 'Luiz Fernando Gomes Soares | Guido Lemos | Sérgio Colcher',
        'Situação: ': 'Disponível',
    },
    {
        'Código:': '065324',
        'Título: ': 'Metodologia Científica',
        'Autor: ': 'Amado L. Cervo | Pedro A. Bervian | Roberto Da Silva',
        'Situação: ': 'Emprestado',
    },
    {
        'Código:': '000065',
        'Título: ': 'Informática conceitos básicos',
        'Autor: ': 'Fernando de Castro Velloso',
        'Situação: ': 'Disponível',
    },
    {
        'Código:': '000236',
        'Título: ': 'Curso Técnico de Hardware',
        'Autor: ': 'José Gouveia | Alberto Magalhães',
        'Situação: ': 'Emprestado',
    },
    {
        'Código:': '045896',
        'Título: ': 'Comom elaborar projetos de Pesquisa',
        'Autor: ': 'Antonio Carlos Gil',
        'Situação: ': 'Disponível',
    },
    {
        'Código:': '013145',
        'Título: ': 'Introdução à Informática',
        'Autor: ': 'Peter Norton',
        'Situação: ': 'Emprestado',
    },
    {
        'Código:': '014797',
        'Título: ': 'Algoritmos',
        'Autor: ': 'Thomas H. Cormen | Charles E. Leiserson | Ronald L. Rivest | Clifford Stein' ,
        'Situação: ': 'Disponível',
    },
    {
        'Código:': '013654',
        'Título: ': 'Java Como Programar',
        'Autor: ': 'H. M. Deitel | P. J. Deitel',
        'Situação: ': 'Disponível',
    },
    {
        'Código:': '132468',
        'Título: ': 'Processamento de Dados',
        'Autor: ': 'Tamio Shimizu',
        'Situação: ': 'Disponível',
    },
    
]
usuario = []

#Bloco feito por André Cristian (cadastro de livros)
def cadastrar_livro():   
    print('\nPara cadastrar o livro você precisa das seguites informações: \n')

    código = input('Código do livro: ') 
    titulo = input('Título do livro: ') 
    autor = input('Autor do Livro: ')

    tratamento_situacao = input('\nO livro está disponível ? [s/n]: ').lower()
    if (tratamento_situacao == 's'):
        situacao = 'Disponível'
    else:
        situacao = 'Emprestado'

    novo_livro = {
        'Código: ': código,
        'Título: ': titulo,
        'Autor: ': autor,
        'Situação: ': situacao
    }
    
    bibliteca.append(novo_livro)
            
    return '\nLivro cadastrado com sucesso!!'

#Bloco feito por André Cristian (cadastro de usuários)
def cadastrar_usuario():
    print('\nPara cadastrar um usuário precisa das seguintes informações: \n')

    nome = input('Digite o nome do usuário: ')
    matricula = int(input('Digite a matrícula do usuário: '))

    novo_usuario = {
        'Usuário: ': nome,
        'Matrícula: ': matricula
    }

    usuario.append(novo_usuario)

    return '\nUsuário cadastrado com sucesso!!'


match resultado:
    case 1:
        #Bloco feito por André Cristian
        cadastro_livro = input('\nVocê deseja cadastrar um livro [s/n] ?: ').lower()

        if (cadastro_livro == 's'):
            mensagem = cadastrar_livro()
            print(mensagem)
        elif (cadastro_livro == 'n'):
            print('Volte quando precisar cadastrar um livro!')
        else:
            print('Você digitou uma resposta invalida, reinicie o sistema e tente novamente.')
    case 2:
        #Bloco feito por André Cristian
        cadastro_usuario = input('\nVocê deseja cadastrar um usuário [s/n] ?: ').lower()

        if(cadastro_usuario == 's'):
            mensagem = cadastrar_usuario()
            print(mensagem)
        elif(cadastro_usuario == 'n'):
            print('Volte quando precisar cadastrar um usuário!')
        else:
            print('Você digitou uma resposta invalida, reinicie o sistema e tente novamente.')

    case 3:
        print('Resgistre o emprestimo do livro')
        #Bloco feito por João Gabriel Lima
         \\ Registrar empréstimo informando a data (DD/MM) e calcular a data de devolução. 


dia = int(input("Dia do empréstimo: "))
mes = int(input("Mês do empréstimo: "))

prazo = 7

dias_mes = [31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]

dia = dia + prazo

if dia > dias_mes[mes - 1]:
    dia = dia - dias_mes[mes - 1]
    mes = mes + 1

    if mes > 12:
        mes = 1

print("Data da devolução:", dia, "/", mes)
    case 4:
        print('Registre a devolução do livro')
    case 5:
        # Bloco feito por Luis Felipe - Livros disponíveis
        print('\n========== LIVROS DISPONÍVEIS ==========')

        quantidade = 0

        for livro in bibliteca:
            if livro['Situação: '] == 'Disponível':
                quantidade += 1

                codigo = livro.get('Código:', livro.get('Código: ', 'Não informado'))

                print(f"\nCódigo: {codigo}")
                print(f"Título: {livro['Título: ']}")
                print(f"Autor: {livro['Autor: ']}")

        if quantidade == 0:
            print('\nNenhum livro disponível no momento.')
        else:
            print(f'\nTotal de livros disponíveis: {quantidade}')

    case 6:
        # Bloco feito por Luis Felipe - Livros emprestados
        print('\n========== LIVROS EMPRESTADOS ==========')

        quantidade = 0

        for livro in bibliteca:
            if livro['Situação: '] == 'Emprestado':
                quantidade += 1

                codigo = livro.get('Código:', livro.get('Código: ', 'Não informado'))

                print(f"\nCódigo: {codigo}")
                print(f"Título: {livro['Título: ']}")
                print(f"Autor: {livro['Autor: ']}")

                responsavel = livro.get('Usuário: ', 'Não informado')
                print(f"Emprestado para: {responsavel}")

        if quantidade == 0:
            print('\nNenhum livro emprestado no momento.')
        else:
            print(f'\nTotal de livros emprestados: {quantidade}')
    case 7:
        print('Vou listar todos os emprestimos atrasados')
    case _:
        print('Você selecionou um serviço inválido')

