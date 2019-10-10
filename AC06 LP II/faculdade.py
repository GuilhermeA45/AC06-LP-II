# Linguagem de Programação II
# AC06 ADS2D - Faculdade
# alunos: lucas.cristovam@aluno.faculdadeimpacta.com.br
#         guilherme.asantos@aluno.faculdadeimpacta.com.br


class Disciplina:
    '''
    Abstração de uma disciplinai, possui os atributos Nome e carga Horária
    '''
    def __init__(self, nome: str, carga_horaria: int) -> None:
        self._nome = nome
        self._carga_horaria = carga_horaria

    def get_nome(self) -> str:
        '''
        Acessor do atributo nome
        '''
        return self._nome

    def get_carga_horaria(self) -> int:
        '''
        Acessor do atributo cargar horaria
        '''
        return self._carga_horaria


class Pessoa:
    '''
    Abstração de uma pessoa no Modelo, classe base para Aluno e Professor
    que contém dados pertencentes a ambos.
    '''
    def __init__(self, nome: str, telefone: int, email: float) -> None:
        self._nome_pessoa = nome
        self._telefone = telefone
        if type(self._telefone) is not int:
            raise TypeError('Telefone inválido')
        self._email = email
        lista_email = list(self._email)
        if '@' not in lista_email:
            raise ValueError('E-mail inválido')

    def get_nome(self) -> str:
        '''
        Acessor do atributo Nome
        '''
        return self._nome_pessoa

    def get_telefone(self) -> int:
        '''
        Acessor do atributo telefone
        '''
        return self._telefone

    def set_telefone(self, novo_telefone: int) -> None:
        '''
        Mutador do atributo telefone deve checar se é um número inteiro e,
        caso contrário devolver um TypeError
        '''
        self.novo_telefone = novo_telefone
        if type(self.novo_telefone) is not int:
            raise TypeError('Digite um número válido')
        self._telefone = self.novo_telefone

    def get_email(self) -> str:
        '''
        Acessor do atributo email
        '''
        return self._email

    def set_email(self, novo_email) -> None:
        '''
        Mutador do atributo eail, deve checar se éum email válido
        (se possuir o caractere '@') e caso contrário devolver
        um ValueError
        '''
        self.novo_email = novo_email
        lista_nemail = list(self.novo_email)
        if '@' not in lista_nemail:
            raise ValueError('Digite um e-mail válido')
        self._email = self.novo_email


class Aluno(Pessoa):

    def __init__(self, nome: str, telefone: int,
                 email: str, n_matricula: int) -> None:
        pass

    def get_matricula(self) -> int:
        '''
        Acessor do atributo matricula
        '''
        pass

    def matricular(self, disciplina: Disciplina) -> None:
        '''
        Realiza matrícula do Aluno na disciplina
        '''
        pass

    def lista_disciplinas(self) -> list:
        '''
        Devolve a lista de disciplinas em que o aluno esta matriculado
        '''
        pass


class Professor(Pessoa):
    '''
    Entidade professor do Modelo
    '''
    def __init__(self, nome, telefone, email):
        pass

    def ministra(self, disciplina: Disciplina) -> None:
        '''
        Atribui o professor como ministrante da disiciplina
        Um professor não pode dar mais de 200 horas de aula,
        Caso um professor tente atribuir mais de 200h devolve
        ValueError
        '''
        pass

    def lista_disciplinas(self) -> list:
        '''
        lista as disciplinas ministradas pelo professor
        '''
        pass
