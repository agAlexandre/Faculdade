class Pessoa:
    def __init__(self,nome,rg,email,telefone):
        self.nome=nome #publico
        self.__rg= rg#privado
        self._email = email #protegido
        self.__telefone = telefone #privado
    def __str__(self):
        return 'Nome:' +self.nome + ',RG: ' + self.__rg +\
    ',Email: ' + self._email + ',Telefone ' + self.__telefone

    

p= Pessoa('Menezes','123','menezes@gmail','(11)975177517')
print('Objeto: ',p)
print('Nome: ',p.nome)
print('E-mail: ',p._email)
print('RG: ', p._Pessoa__rg)
print('Telefone: ',p._Pessoa__telefone)
