#Exemplo de herança
class Pessoa:
    def __init__(self, nome, rg, email, telefone):
        #Atributos protegidos
        self._nome = nome
        self._rg = rg
        self._email = email
        self._telefone = telefone

    def __str__(self):
        return 'Nome: ' + self._nome + ', RG: ' + self._rg +\
               ', E-mail: ' + self._email + ', Telefone: ' +\
               self._telefone

class Aluno(Pessoa):
    def __init__(self, nome, rg, email, telefone, ra, curso):
        Pessoa.__init__(self, nome, rg, email, telefone)
        self.__ra = ra
        self.__curso = curso

    def __str__(self):
        return 'Nome: ' + self._nome + ', RG: ' + self._rg +\
               ', E-mail: ' + self._email + ', Telefone: ' +\
               self._telefone + '\nRA: ' + self.__ra +\
               ', Curso: ' + self.__curso

a = Aluno('Paulo', '1234', 'paulo@gmail', '123456', '98765',\
          'ADS')
print(a)







        
