# listas vazias para acrescentar os valores
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


''''''

'''login'''


def login():
    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    '''index serve para retornar
    já o append para add 
    '''
    if nome in nomes:
        opa = nomes.index(nome)
        if senhas[opa] == senha:
            print("Login realizado com sucesso!")
        else:
            print("Senha incorreta, tente novamente.")
    else:
        print("Usuário não encontrado.")


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