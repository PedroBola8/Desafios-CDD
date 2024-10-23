#listas vazias para acrescentar os valores
nomes = []
senhas = []
tamanho = len(nomes)

'''cadastro'''

def cadastro():
    novonome = input("Digite o nome do novo usuário: ")
    if novonome in nomes:
        print("Usuário já existe! Tente outro nome.")
    else:
        novasenha = input("Digite sua senha: ")
        nomes.append(novonome)
        senhas.append(novasenha)
        print(f"Usuário {novonome} cadastrado com sucesso!")



'''login'''

def login():
    if len(nomes) == 0:
        print("Nenhum usuário cadastrado.")
    else:
        print("Usuários cadastrados:")
        nome = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")

        if nome in nomes:
            opa = nomes.index(nome)
            if senhas[opa] == senha:
                print("Login realizado com sucesso!")
            else:
                print("Senha incorreta, tente novamente.")

        else:
            print("Usuário não encontrado.")

    '''index serve para retornar
    já o append para add 
    '''


def mostrar():
    if len(nomes) == 0:
        print("Nenhum usuário cadastrado.")
    else:
        print("Usuários cadastrados:")
        for nome in nomes:
            print(f"- {nome}")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Cadastrar")
        print("2. Login")
        print("3. Mostrar usuários")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastro()
        elif opcao == "2":
            login()
        elif opcao == "3":
            mostrar()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()










'''
for i in range(1):
    nomelogin = str(input("Digite seu usuario : "))

if nomelogin in nomes:
    indice = nomes.index(nomelogin)
    indice = nomes.index(nomes)

    print(f"Olá {nomelogin}")

    for t in range(1):
        senhalogin = int(input("Digite sua senha : "))'''



'''else:
    print("Usuário não encontrado")
'''




'''if nomes[x] in nomes:
        print("Olá Pedro!")
        if senha1 == senhas[0]:
            print("Acesso Liberado")
        elif senha1 != senhas[0]:
            print("Acesso Negado")

    elif nome1 == nomes[1]:
            print("Olá Talita")
            for y in range(1):
                senha1 = int(input("Digite sua senha : "))
                if senha1 == senhas[1]:
                    print("Acesso liberado Talita!")
                else:
                    print("Acesso Negado")

    elif nome1 == nomes[2]:
            print("Olá Augusto")
            for t in range(1):
                senha1 = int(input("Digite sua senha : "))
                if senha1 == senhas[2]:
                    print("Acesso Liberado Augusto")
                else:
                    print("Acesso negado")
    else:
        print("Nome Inválido")
'''