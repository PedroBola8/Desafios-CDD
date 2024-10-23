class Atleta:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
        self.aposentado = False
        self.aquecido = False

    def aposentar(self):
        if not self.aposentado:
            print(f'{self.nome} foi se aposentar.')
            self.aposentado = True
        else:
            print(f'{self.nome} já está aposentado.')

    def aquecer(self):
        if not self.aquecido:
            print(f'{self.nome} foi se aquecer.')
            self.aquecido = True
        else:
            print(f'{self.nome} já está aquecido.')


class Corredor(Atleta):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)

    def correr(self):
        if self.aquecido == False:
            if self.aposentado == False:
                print(f'{self.nome} foi correr.')
            else:
                print(f'{self.nome} já está aposentado.')
        else:
            print(f'{self.nome} foi se aquecer.')


class Nadador(Atleta):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)

    def nadar(self):
        if self.aquecido == False:
            if self.aposentado == True:
                print(f'{self.nome} foi nadar.')
            else:
                print(f'{self.nome} já está aposentado.')
        else:
            print(f'{self.nome} foi se aquecer.')


class Ciclista(Atleta):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)

    def pedalar(self):
        if self.aquecido == True:
            if self.aposentado == False:
                print(f'{self.nome} foi pedalar.')
            else:
                print(f'{self.nome} já está aposentado.')
        else:
            print(f'{self.nome} foi se aquecer.')
