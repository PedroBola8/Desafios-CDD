nomes = ["Pedro", "Talita", "Augusto" ]
senhas = [ "123", "1234","12345"]
tamanho = len(nomes)

for login in range(tamanho):
    nomes[login]= str(input("Digite seu nome : "))
    if nomes[login] == nomes[0]:
        print("Olá Pedro!")
        for i in range(1):
            senhas[i] = int(input("Digite sua senha : "))
            if senhas[i] == senhas[0]:
                print("Acesso Liberado Pedro")
            elif senhas[i] != senhas[0]:
                print("Acesso Negado")

    elif nomes[login] == nomes[1]:
        print("Olá Talita")
        for y in range(1):
            senhas[y] = int(input("Digite sua senha : "))
            if senhas[y] == senhas[1]:
                print("Acesso liberado Talita!")
            else:
                print("Acesso Negado")

    elif nomes[login] == nomes[2]:
        print("Olá Augusto")
        for t in range(1):
            senhas[t] = int(input("Digite sua senha : "))
            if senhas[t]== senhas[2]:
                print("Acesso Liberado Augusto")
            else:
                print("Acesso negado")
    else:
        print("Nome Inválido")


'''nome = [0]*1
senha = ["0066"]
tamanho = len(nome)


for cadastro in range(tamanho):
    nome[cadastro]= str(input("Digite o usuario : "))
    senha[cadastro] = int(input("Digite sua senha : "))

for login in range(tamanho):
    nome[login] = str(input("Digite seu usuario : "))


    if nome[login] == nome[cadastro]:
        print("Olá Pedro")
        senha[login] = int(input("Digite sua senha pfvr : "))

        if senha[login] == senha[0]:
            print("Acesso liberado Pedro!")

        else:
            print("Senha incorreta")'''


'''for x in range(3):
    print(f"{x}: nome: {nome[x]}, senha: {senha[x]}")




num = [0]*10
tamanho = len(num)
cont = 0
num2 = 0

for x in range(tamanho):
    num[x]= int(input("Digite um N° : "))

num2 = int(input("Digite mais um N° : "))

for i in range(tamanho):
    if num2 == num[x]:
        cont +=1
print(cont)'''