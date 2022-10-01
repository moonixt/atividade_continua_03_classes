
class Pessoa:
    def __init__(self, nome: str, nascimento: str):
        self.nome = nome
        self.nascimento = nascimento


class Professor(Pessoa):
    def __init__(self, nome: str, nascimento: str):
        super().__init__(nome, nascimento)
        self.disciplinas = []

    def incluir_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)


class Disciplina:
    def __init__(self, nome: str, ementa: str):
        self.nome = nome
        self.ementa = ementa


class Aluno(Pessoa):
    def __init__(self, nome: str, nascimento: str, tipo: str, casa=None,
                 triunfos=0, mau_feitos=0):
        super().__init__(nome, nascimento)
        self.tipo = tipo
        self.casa = casa
        self.disciplinas = []
        self.__triunfos = triunfos
        self.__mau_feitos = mau_feitos

    def incluir_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def set_casa(self, casa):
        self.casa = casa

    def incluir_triunfo(self, quantidade):
        self.__triunfos = quantidade

    def incluir_mau_feito(self, quantidade):
        self.__mau_feitos = quantidade

    def get_triunfos(self):
        return self.__triunfos

    def get_mau_feitos(self):
        return self.__mau_feitos


class Casa:
    def __init__(self, nome: str, animal: str, diretor=None, monitor=None):
        self.nome = nome
        self.animal = animal
        self.__diretor = diretor
        self.__monitor = monitor

    def set_diretor(self, diretor):
        self.__diretor = diretor

    def set_monitor(self, monitor):
        self.__monitor = monitor

    def get_diretor(self):
        return self.__diretor

    def get_monitor(self):
        return self.__monitor


class Escola:
    def __init__(self, nome: str):
        self.nome = nome
        self.casas = []

    def incluir_casa(self, casa):
        self.casas.append(casa)


class Torneio:
    def __init__(self, casa1: str, casa2: str, pontos_casa1=0, pontos_casa2=0):
        self.casa1 = casa1
        self.casa2 = casa2
        self.__pontos_casa1 = pontos_casa1
        self.__pontos_casa2 = pontos_casa2

    def marcar_ponto(self, casa: str, quantidade: str):
        self.casa = casa
        self.quantidade = quantidade
        if self.casa == self.casa1:
            self.__pontos_casa1 += self.quantidade
            return self.__pontos_casa1
        elif self.casa == self.casa2:
            self.__pontos_casa2 += self.quantidade
            return self.__pontos_casa2

    def get_pontos_casa1(self):
        return self.__pontos_casa1

    def get_pontos_casa2(self):
        return self.__pontos_casa2
