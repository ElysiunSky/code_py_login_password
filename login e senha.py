'''
login em bloco de notas
'''
# by ferreirajk8@gmail.com
# gitHub: ElysiunSky
# courses: Voip Asterisk (call in pv)
# This code is a complete open source for Python community
# not is a code to implementation real, just a code of study and pratices
# não é permitida a venda desse código para lucro pessoal, o código é total aberto ao uso grátis ao público


from ast import While

# hash falsa criada para ressaltar que pode-se implementar um gerador de hash aleatórias em python, e armazena-la no arquivo "registrados.txt" junto com login e senha
hash = 'ola12usurio12essasuahash2023'


#def de login, após o usuário passar pelo def de cadastro, agora seus dados já se encontram armazenados no arquivo "registrados.txt", sendo assim, esse def de login irá buscar o usuário para realizar o log atual
def login():
    arq = open('registrados.txt')
    login = str(input('Login: '))
    senha = str(input('Senha: '))
    registrados = arq.readlines()
    if login + hash + senha + '\n' in registrados:
        arq = open('registrados.txt')
        print('\n\nOlá, Seja Bem-Vindo (a) {}!!\n\n'.format(login))
               
    else:
        print('Usuário ou Senha Incorretos!')        


# def para realizar a depuração do login e senha, verificar se já é existente no arquivo de dados
def dep():
    arq = open('registrados.txt','a')
    arq = open('registrados.txt')
    login = str(input('Nome de usuario: '))
    senha = input('Cadastre uma senha: ')
    registrados = arq.readlines()   
    if login + hash + senha + '\n' in registrados:
        arq = open('registrados.txt')
        print('Usuário já em uso, por favor, tente outro  nome!')
    else:
        cadastro()


# def de cadastro, esse def tem a função de realizar o cadastro de novos usuário, após o usuário passar pela análise do def de deupuração (def dep())
def cadastro():   
    arq = open('registrados.txt','a')
    nome = input('Confirme Usuário: ')
    senha = input('Confirme a sua senha: ')
    arq.write('{}{}{}\n'.format(nome,hash,senha))
    print('\nCadastro realizado com sucesso!\n')
    arq.close()


# Menu simples que direcionará o usuário entre as opções disponiveis
while True:
    menu = int(input('1- Login\n2- Cadastrar novo usuário\n'))
    if menu == 1:
        login()

    elif menu == 2:
        dep()








'''
                                            Atenção!!
É possível realizar essa implementação usando formas mais seguras, formas essas que podem ser encontradas 
em bibliotecas, ou implementar esse código usando banco de dados, como por exemplo, mysql.
'''
