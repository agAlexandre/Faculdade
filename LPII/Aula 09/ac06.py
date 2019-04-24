'''Criar um código para a seguinte situação: uma super classe Figura, 
com os atributos coordenadax, coordenaday, corLinha, corFundo, escala; duas classes derivadas (filhas), 
Círculo (atributo raio e método de cálculo de área) 
e Quadrado (atributo lado e método de cálculo de área apropriado).'''

class Figura ():
    def __init__(self,coordenadax,coordenaday,corLinha,corFundo,escala):
        self._coordenadax= coordenadax 
        self._coordenaday= coordenaday
        self._corLinha= corLinha
        self._corFundo= corFundo
        self._escala= escala
    def __str__ (self):
         return 'Coordenada X: ' + self._coordenadax + ', Coordenada Y: ' + self._coordenaday + ', Cor da Linha: ' + self._corLinha + ', Cor de Fundo: ' + self._corFundo + ', Escala: ' + self._escala
         
class Circulo(Figura):
    def __init__(self, raio, metodoCalculoRaio):
        Figura.__init__(self,coordenadax,coordenaday,corLinha,corFundo,escala)
        self.raio = raio

    def metodoCalculoRaio(self):
        return 3.14*(self.raio*self.raio)
    
    def __str__(self):
        return 'Valor do Raio: ' + self.metodoCalculoRaio()


class Quadrado(Figura):
    def __init__ (self,lado, metodoCalculoQuadrado):
        Figura.__init__(self,coordenadax,coordenaday,corLinha,corFundo,escala)
        self.__lado = lado

    def metodoCalculoQuadrado(self, lado):
        self.__area = lado*lado

    def __str__(self):
        return 'Valor do quadrado: ' + metodoCalculoQuadrado() 
