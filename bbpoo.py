class Pessoa:
    def __init__(self, peso, nome, idade):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.comendo = False
        self.dormindo = False
        self.falando = False

    def comer(self, comida):
        if self.comendo:
            print(f"{self.nome} já está comendo.")
        elif self.falando:
            print(f"{self.nome} não pode comer porque está falando.")
        elif self.dormindo:
            print(f"{self.nome} não pode comer porque está dormindo.")
        else:
            print(f"{self.nome} foi comer {comida}.")
            self.comendo = True
            self.dormindo = False
            self.falando = False

    def falar(self):
        if self.comendo:
            print(f"{self.nome} não pode falar porque está comendo.")
        elif self.dormindo:
            print(f"{self.nome} não pode falar porque está dormindo.")
        else:
            print(f"Meu nome é {self.nome}, tenho {self.idade} anos e peso {self.peso}kg.")
            self.falando = True
            self.comendo = False
            self.dormindo = False

    def dormir(self):
        if self.comendo:
            print(f"{self.nome} não pode dormir porque está comendo.")
        elif self.falando:
            print(f"{self.nome} não pode dormir porque está falando.")
        else:
            print(f"{self.nome} foi dormir.")
            self.dormindo = True
            self.comendo = False
            self.falando = False