
def semrepetir(numeros):
    num = []
    sem = []


    for x in range(5):
        N = int(input("Digite um número: "))
        num.append(N)
        '''append serve para add elementos num array/lista'''

    for i in num:
        if i not in sem:  # Se o número não está na lista 'sem', adiciona
            sem.append(i)
    '''novamente usando a função append(add), vamos colocar os N°´s dentro de uma nova lista\n
    sem não repeti-los, então atraves do for pegamos a lista anterior com od dados fornecidos pelo user e \n
    criamos uma condicional, se o N° tal da lista A NÃO estiver na lista B, adicioneo a lista, se estiver,\n
    passa pro próx'''

    print("Lista original:", num)
    print("Lista sem duplicatas:", sem)




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
def stopa():
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

